import base64
import logging
import math
import time

from actingweb import actor, trust
from actingweb import config as config_class
from actingweb.constants import TRUSTEE_CREATOR

# This is where each path and subpath in actingweb is assigned an authentication type
# Currently only basic auth is supported. OAuth2 peer auth is automatic if an Authorization Bearer <token> header is
# included in the http request.



def add_auth_response(appreq=None, auth_obj=None):
    """Called after authentication to set appropriate HTTP response based on auth result."""
    if not appreq or not auth_obj:
        return False
    logging.debug(
        "add_auth_response: "
        + str(auth_obj.response["code"])
        + ":"
        + auth_obj.response["text"]
    )
    logging.debug(f"add_auth_response: auth_obj.redirect = {getattr(auth_obj, 'redirect', None)}")
    appreq.response.set_status(auth_obj.response["code"], auth_obj.response["text"])
    if auth_obj.response["code"] == 302:
        logging.debug(f"add_auth_response: Setting redirect to {auth_obj.redirect}")
        appreq.response.set_redirect(url=auth_obj.redirect)
    elif auth_obj.response["code"] == 401:
        if hasattr(appreq, 'response') and appreq.response:
            if hasattr(appreq.response, 'write'):
                appreq.response.write("Authentication required")
            else:
                appreq.response.body = "Authentication required"
    for h, v in list(auth_obj.response["headers"].items()):
        if hasattr(appreq, 'response') and appreq.response:
            appreq.response.headers[h] = v
    return True




class Auth:
    """The auth class handles authentication and authorisation for the various schemes supported.

    The check_authentication() function checks the various authentication schemes against the path and does proper
    authentication.
    There are two types supported: basic (using creator credentials) and token (received when trust is created or OAuth2).
    The check_authorisation() function validates the authenticated user against the config.py access list.
    check_token_auth() can be called from outside the class to do a simple peer/bearer token verification.

    The response[], acl[], and authn_done variables are useful outside Auth(). authn_done is set when authentication has
    been done and a final authentication status can be found in response[].

         self.response = {

            "code": 403,                # Result code (http)
            "text": "Forbidden",        # Proposed response text
            "headers": [],              # Headers to add to response after authentication has been done

        }

        self.acl = {

            "authenticated": False, # Has authentication been verified and passed?
            "authorised": False,    # Has authorisation been done and appropriate acls set?
            "rights": '',           # "a", "r" (approve or reject)
            "relationship": None,   # E.g. creator, friend, admin, etc
            "peerid": '',           # Peerid if there is a relationship
            "approved": False,      # True if the peer is approved

        }

    """

    def __init__(self, actor_id, auth_type="basic", config=None):
        if not config:
            self.config = config_class.Config()
        else:
            self.config = config
        self.token = None
        self.type = auth_type
        self.trust = None
        # Proposed response code after check_authentication() or authorise() have been called
        self.response = {"code": 403, "text": "Forbidden", "headers": {}}
        # Whether authentication is complete or not (depends on flow)
        self.authn_done = False
        # acl stores the actual verified credentials and access rights after
        # authentication and authorisation have been done
        self.acl = {
            "authenticated": False,  # Has authentication been verified and passed?
            "authorised": False,  # Has authorisation been done and appropriate acls set?
            "rights": "",  # "a", "r" (approve or reject)
            "relationship": None,  # E.g. creator, friend, admin, etc
            "peerid": "",  # Peerid if there is a relationship
            "approved": False,  # True if the peer is approved
        }
        self.actor = actor.Actor(actor_id, config=self.config)
        if not self.actor.id:
            self.actor = None
            return
        if self.type == "basic":
            self.realm = self.config.auth_realm


    def __check_basic_auth_creator(self, appreq):
        if self.type != "basic":
            logging.warning("Trying to do basic auth when auth type is not basic")
            self.response["code"] = 403
            self.response["text"] = "Forbidden"
            return False
        if not self.actor or not self.actor.passphrase:
            logging.warning(
                "Trying to do basic auth when no passphrase value can be found."
            )
            self.response["code"] = 403
            self.response["text"] = "Forbidden"
            return False
        if "Authorization" not in appreq.request.headers:
            self.response["headers"]["WWW-Authenticate"] = (
                'Basic realm="' + self.realm + '"'
            )
            self.response["code"] = 401
            self.response["text"] = "Authentication required"
            return False
        authz = appreq.request.headers["Authorization"]
        (basic, token) = authz.split(" ")
        if basic.lower() != "basic":
            self.response["code"] = 403
            self.response["text"] = "No basic auth in Authorization header"
            logging.debug("No basic auth in Authorization header")
            return False
        self.authn_done = True
        au = authz.split(" ")[1]
        au = au.encode("utf-8")
        au = base64.b64decode(au)
        (username, password) = au.split(b":")
        password = password.decode("utf-8")
        username = username.decode("utf-8")
        if not self.actor or username != self.actor.creator:
            self.response["code"] = 403
            self.response["text"] = "Invalid username or password"
            logging.debug("Wrong creator username")
            return False
        if not self.actor or password != self.actor.passphrase:
            self.response["code"] = 403
            self.response["text"] = "Invalid username or password"
            logging.debug(
                "Wrong creator passphrase("
                + password
                + ") correct("
                + (self.actor.passphrase if self.actor else "")
                + ")"
            )
            return False
        self.acl["relationship"] = "creator"
        self.acl["authenticated"] = True
        self.response["code"] = 200
        self.response["text"] = "Ok"
        return True

    def check_token_auth(self, appreq):
        """Called with an http request to check the Authorization header and validate if we have a peer with
        this token."""
        if "Authorization" not in appreq.request.headers:
            return False
        auth = appreq.request.headers["Authorization"]
        auth_parts = auth.split(" ")
        if len(auth_parts) != 2 or auth_parts[0].lower() != "bearer":
            return False
        token = auth_parts[1]
        self.authn_done = True
        
        # First, try OAuth2 authentication if configured
        if self._check_oauth2_token(token):
            return True
        
        trustee = self.actor.store.trustee_root if self.actor and self.actor.store else None
        # If trustee_root is set, creator name is 'trustee' and
        # bit strength of passphrase is > 80, use passphrase as
        # token
        if trustee and self.actor and self.actor.creator and self.actor.creator.lower() == TRUSTEE_CREATOR:
            if self.actor.passphrase and math.floor(len(self.actor.passphrase) * math.log(94, 2)) > 80:
                if token == self.actor.passphrase:
                    self.acl["relationship"] = TRUSTEE_CREATOR
                    self.acl["peerid"] = ""
                    self.acl["approved"] = True
                    self.acl["authenticated"] = True
                    self.response["code"] = 200
                    self.response["text"] = "Ok"
                    self.token = self.actor.passphrase if self.actor else None
                    return True
            else:
                logging.warning(
                    "Attempted trustee bearer token auth with <80 bit strength token."
                )
        tru = trust.Trust(actor_id=self.actor.id if self.actor else None, token=token, config=self.config)
        new_trust = tru.get()
        if new_trust:
            logging.debug("Found trust with token: (" + str(new_trust) + ")")
            if self.actor and new_trust["peerid"] == self.actor.id:
                logging.error("Peer == actor!!")
                return False
        if new_trust and len(new_trust) > 0:
            self.acl["relationship"] = new_trust["relationship"]
            self.acl["peerid"] = new_trust["peerid"]
            self.acl["approved"] = new_trust["approved"]
            self.acl["authenticated"] = True
            self.response["code"] = 200
            self.response["text"] = "Ok"
            self.token = new_trust["secret"]
            self.trust = new_trust
            return True
        else:
            return False

    def _check_oauth2_token(self, token):
        """Check if the Bearer token is a valid OAuth2 token and authenticate user."""
        try:
            from .oauth2 import create_oauth2_authenticator
            authenticator = create_oauth2_authenticator(self.config)
            
            if not authenticator.is_enabled():
                return False
            
            # Validate token and get user info
            user_info = authenticator.validate_token_and_get_user_info(token)
            if not user_info:
                return False
                
            # Extract email from user info
            email = authenticator.get_email_from_user_info(user_info)
            if not email:
                return False
            
            # For OAuth2, we authenticate users based on their email
            # The actor lookup is handled at the endpoint level, not here in auth
            # Here we just validate that the token is valid and get the email
            
            # Check if this is the correct actor for this email (when actor_id is provided in URL)
            if self.actor and self.actor.creator and self.actor.creator.lower() == email.lower():
                # This is the correct actor for this email
                self.acl["relationship"] = "creator"
                self.acl["peerid"] = ""
                self.acl["approved"] = True
                self.acl["authenticated"] = True
                self.response["code"] = 200
                self.response["text"] = "Ok"
                self.token = token
                logging.debug(f"OAuth2 authentication successful for {email}")
                return True
            else:
                # Email doesn't match this actor - this could be:
                # 1. Wrong actor for this user
                # 2. New user (actor creation flow handles this)
                # 3. Factory endpoint (no specific actor yet)
                logging.debug(f"OAuth2 email {email} doesn't match actor creator {self.actor.creator if self.actor else 'None'}")
                
                # For factory endpoint or when no actor is loaded, we still consider auth successful
                # The endpoint handler will use get_by_creator() to find/create the right actor
                if not self.actor:
                    self.acl["relationship"] = "creator"
                    self.acl["peerid"] = ""
                    self.acl["approved"] = True
                    self.acl["authenticated"] = True
                    self.response["code"] = 200
                    self.response["text"] = "Ok"
                    self.token = token
                    logging.debug(f"OAuth2 authentication successful for {email} (no specific actor)")
                    return True
                
                return False
                
        except Exception as e:
            logging.error(f"Error during OAuth2 token validation: {e}")
            return False

    def _should_redirect_to_oauth2(self, appreq, path):
        """Check if we should redirect to OAuth2 for authentication."""
        try:
            from .oauth2 import create_oauth2_authenticator
            authenticator = create_oauth2_authenticator(self.config)
            
            if not authenticator.is_enabled():
                return False
            
            # Don't redirect for OAuth callback URLs to avoid infinite loops
            if "/oauth/callback" in path:
                return False
            
            # Create redirect to OAuth2
            original_url = self._get_original_url(appreq, path)
            auth_url = authenticator.create_authorization_url(redirect_after_auth=original_url)
            
            if auth_url:
                self.authn_done = True
                self.response["code"] = 302
                self.response["text"] = "Redirecting to OAuth2"
                self.redirect = auth_url
                logging.debug(f"Redirecting to OAuth2: {auth_url[:100]}...")
                return True
                
        except Exception as e:
            logging.error(f"Error creating OAuth2 redirect: {e}")
        
        return False

    def _get_original_url(self, appreq, path):
        """Get the original URL being accessed for redirect after auth."""
        try:
            # Try to construct the original URL
            if hasattr(appreq, 'request') and hasattr(appreq.request, 'url'):
                return str(appreq.request.url)
            elif hasattr(appreq, 'request') and hasattr(appreq.request, 'uri'):
                return str(appreq.request.uri)
            else:
                # Fallback to constructing from config and path
                return f"{self.config.proto}{self.config.fqdn}{path}"
        except:
            # Last resort fallback
            return f"{self.config.proto}{self.config.fqdn}{path}"

    def check_authentication(self, appreq, path):
        """Checks authentication in appreq, redirecting back to path if oauth is done."""
        logging.debug(f"Checking authentication for path: {path}, auth type: {self.type}")
        logging.debug("Checking authentication, token auth...")
        if self.check_token_auth(appreq):
            logging.debug("Token auth succeeded")
            return
        elif self.type == "basic":
            logging.debug("Auth type is 'basic', checking basic authentication...")
            if self.__check_basic_auth_creator(appreq=appreq):
                logging.debug("Basic auth succeeded, response code: %s", self.response["code"])
                return
            else:
                # Basic auth failed - mark as done and don't fall through to OAuth2
                logging.debug("Basic auth failed, response code: %s", self.response["code"])
                self.authn_done = True
                return
        
        # If all authentication methods fail, try OAuth2 redirect if configured
        logging.debug("All auth methods failed, checking OAuth2 redirect...")
        if self._should_redirect_to_oauth2(appreq, path):
            logging.debug("OAuth2 redirect triggered")
            return
            
        logging.debug("Authentication done, and failed")
        self.authn_done = True
        self.response["code"] = 403
        self.response["text"] = "Forbidden"
        return

    def check_authorisation(
        self, path="", subpath="", method="", peerid="", approved=True
    ):
        """Checks if the authenticated user has acl access rights in config.py.

        Takes the path, subpath, method, and peerid of the path (if auth user
        is different from the peer that owns the path, e.g. creator). If approved
        is False, then the trust relationship does not need to be approved for
        access"""
        # For DELETE operations on trust relationships, always allow deletion regardless of approval status
        # This ensures that broken or partially approved relationships can still be cleaned up
        if (len(self.acl["peerid"]) > 0 and approved and self.acl["approved"] is False and 
            not (path.lower() == "trust" and method.upper() == "DELETE")):
            logging.debug(
                "Rejected authorization because trust relationship is not approved."
            )
            return False
        if self.acl["relationship"]:
            relationship = self.acl["relationship"].lower()
        else:
            relationship = ""
        method = method.upper()
        self.acl["authorised"] = True
        self.acl["rights"] = "r"
        if len(path) == 0:
            return False
        if not subpath:
            subpath = ""
        fullpath = path.lower() + "/" + subpath.lower()
        # ACLs: ('role', 'path', 'METHODS', 'access')
        logging.debug(
            "Testing access for ("
            + relationship
            + " "
            + self.acl["peerid"]
            + ") on ("
            + fullpath
            + " "
            + peerid
            + ") using method "
            + method
        )
        for acl in self.config.access:
            if acl[0] == "any" and not self.acl["authenticated"]:
                continue
            if (
                len(acl[0]) > 0
                and acl[0] != "any"
                and acl[0] != relationship
                and acl[0] != "owner"
            ):
                continue  # no match on relationship
            if (
                acl[0] == relationship
                or acl[0] == "any"
                or len(acl[0]) == 0
                or (
                    acl[0] == "owner"
                    and len(peerid) > 0
                    and self.acl["peerid"] == peerid
                )
            ):
                if fullpath.find(acl[1]) == 0:
                    if len(acl[2]) == 0 or acl[2].find(method) != -1:
                        self.acl["rights"] = acl[3]
                        logging.debug(
                            "Granted " + acl[3] + " access with ACL:" + str(acl)
                        )
                        return True
        return False


def check_and_verify_auth(appreq=None, actor_id=None, config=None):
    """Check and verify authentication for non-ActingWeb routes.

    This function provides authentication verification for custom routes that don't go through
    the standard ActingWeb handler system. It performs authentication checks and is designed
    for use in custom application routes.

    Args:
        appreq: Request object in the format used by ActingWeb handlers.
        actor_id (str | None): Actor ID to verify authentication against.
        config (Config | None): ActingWeb config object.

    Returns:
        dict: A dictionary with the following keys:

        - ``authenticated`` (bool): True if authentication successful.
        - ``actor`` (Actor | None): Actor object when authenticated, otherwise None.
        - ``auth`` (Auth): Auth object with authentication details.
        - ``response`` (dict): Response details: ``{"code": int, "text": str, "headers": dict}``.
        - ``redirect`` (str | None): Redirect URL if authentication requires redirect.

    Example:
        .. code-block:: python

            auth_result = check_and_verify_auth(appreq, actor_id, config)
            if not auth_result['authenticated']:
                if auth_result['response']['code'] == 302:
                    # Redirect for OAuth
                    return redirect(auth_result['redirect'])
                # Return error response
                return error_response(
                    auth_result['response']['code'], auth_result['response']['text']
                )

            # Authentication successful, use auth_result['actor']
            actor = auth_result['actor']
    """
    
    if not config:
        config = config_class.Config()
        
    # Use basic auth type for custom routes (supports both basic and Bearer token auth)
    auth_obj = Auth(actor_id, auth_type="basic", config=config)
    
    result = {
        'authenticated': False,
        'actor': None,
        'auth': auth_obj,
        'response': {'code': 403, 'text': 'Forbidden', 'headers': {}},
        'redirect': None
    }
    
    if not auth_obj.actor:
        result['response'] = {'code': 404, 'text': 'Actor not found', 'headers': {}}
        return result
    
    # Check authentication without modifying the response object
    auth_obj.check_authentication(appreq=appreq, path="/custom")
    
    # Copy response details
    result['response'] = {
        'code': auth_obj.response['code'],
        'text': auth_obj.response['text'],
        'headers': auth_obj.response['headers'].copy()
    }
    
    # Set redirect if needed
    if hasattr(auth_obj, 'redirect') and auth_obj.redirect:
        result['redirect'] = auth_obj.redirect
    
    # Check if authentication was successful
    if auth_obj.acl['authenticated'] and auth_obj.response['code'] == 200:
        result['authenticated'] = True
        result['actor'] = auth_obj.actor
        
    return result
