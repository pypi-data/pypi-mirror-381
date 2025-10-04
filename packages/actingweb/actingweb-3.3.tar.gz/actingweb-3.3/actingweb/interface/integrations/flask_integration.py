"""
Flask integration for ActingWeb applications.

Automatically generates Flask routes and handles request/response transformation.
"""

from typing import TYPE_CHECKING, Any, Dict, Optional, Union
from flask import Flask, request, redirect, Response, render_template
from werkzeug.wrappers import Response as WerkzeugResponse
import logging

from ...aw_web_request import AWWebObj
from ...handlers import (
    callbacks,
    properties,
    meta,
    root,
    trust,
    devtest,
    subscription,
    resources,
    bot,
    www,
    factory,
    methods,
    actions,
    mcp,
    services,
)

if TYPE_CHECKING:
    from ..app import ActingWebApp


class FlaskIntegration:
    """
    Flask integration for ActingWeb applications.

    Automatically sets up all ActingWeb routes and handles request/response
    transformation between Flask and ActingWeb.
    """

    def __init__(self, aw_app: "ActingWebApp", flask_app: Flask):
        self.aw_app = aw_app
        self.flask_app = flask_app

    def setup_routes(self) -> None:
        """Setup all ActingWeb routes in Flask."""

        # Root factory route with OAuth2 authentication
        @self.flask_app.route("/", methods=["GET"])
        def app_root_get() -> Union[Response, WerkzeugResponse, str]:
            # GET requests don't require authentication - show email form
            return self._handle_factory_get_request()

        @self.flask_app.route("/", methods=["POST"])
        def app_root_post() -> Union[Response, WerkzeugResponse, str]:
            # Check if this is a JSON API request or web form request
            is_json_request = request.content_type and "application/json" in request.content_type
            accepts_json = request.headers.get("Accept", "").find("application/json") >= 0

            if is_json_request or accepts_json:
                # Handle JSON API requests with the standard factory handler
                return self._handle_factory_request()
            else:
                # For web form requests, extract email and redirect to OAuth2 with email hint
                return self._handle_factory_post_with_oauth_redirect()

        # OAuth2 callback - handles both ActingWeb and MCP OAuth2 flows
        @self.flask_app.route("/oauth/callback", methods=["GET"])
        def app_oauth2_callback() -> Union[Response, WerkzeugResponse, str]:
            # Handle both Google OAuth2 callback (for ActingWeb) and MCP OAuth2 callback
            # Determine which flow based on state parameter
            from flask import request

            state = request.args.get("state", "")

            # Check if this is an MCP OAuth2 callback (encrypted state)
            try:
                from ...oauth2_server.state_manager import get_oauth2_state_manager

                state_manager = get_oauth2_state_manager(self.aw_app.get_config())
                mcp_context = state_manager.extract_mcp_context(state)

                if mcp_context:
                    # This is an MCP OAuth2 callback
                    return self._handle_oauth2_endpoint("callback")
            except Exception:
                # Not an MCP callback or state manager not available
                pass

            # Default to Google OAuth2 callback for ActingWeb
            return self._handle_oauth2_callback()

        # OAuth2 server endpoints for MCP clients
        @self.flask_app.route("/oauth/register", methods=["POST", "OPTIONS"])
        def oauth2_register() -> Union[Response, WerkzeugResponse, str]:
            return self._handle_oauth2_endpoint("register")

        @self.flask_app.route("/oauth/authorize", methods=["GET", "POST", "OPTIONS"])
        def oauth2_authorize() -> Union[Response, WerkzeugResponse, str]:
            return self._handle_oauth2_endpoint("authorize")

        @self.flask_app.route("/oauth/token", methods=["POST", "OPTIONS"])
        def oauth2_token() -> Union[Response, WerkzeugResponse, str]:
            return self._handle_oauth2_endpoint("token")

        @self.flask_app.route("/oauth/logout", methods=["GET", "POST", "OPTIONS"])
        def oauth2_logout() -> Union[Response, WerkzeugResponse, str]:
            return self._handle_oauth2_endpoint("logout")

        # Bot endpoint
        @self.flask_app.route("/bot", methods=["POST"])
        def app_bot() -> Union[Response, WerkzeugResponse, str]:
            return self._handle_bot_request()

        # MCP endpoint
        @self.flask_app.route("/mcp", methods=["GET", "POST"])
        def app_mcp() -> Union[Response, WerkzeugResponse, str]:
            # For MCP, allow initial handshake without authentication
            # Authentication will be handled within the MCP protocol
            return self._handle_mcp_request()

        # OAuth2 Discovery endpoints using OAuth2EndpointsHandler
        @self.flask_app.route("/.well-known/oauth-authorization-server", methods=["GET", "OPTIONS"])
        def oauth_discovery() -> Union[Response, WerkzeugResponse, str]:
            """OAuth2 Authorization Server Discovery endpoint (RFC 8414)."""
            return self._handle_oauth2_discovery_endpoint(".well-known/oauth-authorization-server")

        @self.flask_app.route("/.well-known/oauth-protected-resource", methods=["GET", "OPTIONS"])
        def oauth_protected_resource_discovery() -> Union[Response, WerkzeugResponse, str]:
            """OAuth2 Protected Resource discovery endpoint."""
            return self._handle_oauth2_discovery_endpoint(".well-known/oauth-protected-resource")

        @self.flask_app.route("/.well-known/oauth-protected-resource/mcp", methods=["GET", "OPTIONS"])
        def oauth_protected_resource_mcp_discovery() -> Union[Response, WerkzeugResponse, str]:
            """OAuth2 Protected Resource discovery endpoint for MCP."""
            return self._handle_oauth2_discovery_endpoint(".well-known/oauth-protected-resource/mcp")

        # MCP information endpoint
        @self.flask_app.route("/mcp/info", methods=["GET"])
        def mcp_info() -> Dict[str, Any]:
            """MCP information endpoint."""
            return self._create_mcp_info_response()

        # Actor root
        @self.flask_app.route("/<actor_id>", methods=["GET", "POST", "DELETE"])
        def app_actor_root(actor_id: str) -> Union[Response, WerkzeugResponse, str]:
            # Align with FastAPI: protect actor root with OAuth when enabled
            auth_redirect = self._check_authentication_and_redirect()
            if auth_redirect:
                return auth_redirect
            return self._handle_actor_request(actor_id, "root")

        # Actor meta
        @self.flask_app.route("/<actor_id>/meta", methods=["GET"])
        @self.flask_app.route("/<actor_id>/meta/<path:path>", methods=["GET"])
        def app_meta(actor_id: str, path: str = "") -> Union[Response, WerkzeugResponse, str]:
            return self._handle_actor_request(actor_id, "meta", path=path)


        # Actor www with OAuth2 authentication
        @self.flask_app.route("/<actor_id>/www", methods=["GET", "POST", "DELETE"])
        @self.flask_app.route("/<actor_id>/www/<path:path>", methods=["GET", "POST", "DELETE"])
        def app_www(actor_id: str, path: str = "") -> Union[Response, WerkzeugResponse, str]:
            # Check authentication and redirect to OAuth2 if needed
            auth_redirect = self._check_authentication_and_redirect()
            if auth_redirect:
                return auth_redirect
            return self._handle_actor_request(actor_id, "www", path=path)

        # Actor properties
        @self.flask_app.route("/<actor_id>/properties", methods=["GET", "POST", "DELETE", "PUT"])
        @self.flask_app.route("/<actor_id>/properties/<path:name>", methods=["GET", "POST", "DELETE", "PUT"])
        def app_properties(actor_id: str, name: str = "") -> Union[Response, WerkzeugResponse, str]:
            # Align with FastAPI: protect properties with OAuth when enabled
            auth_redirect = self._check_authentication_and_redirect()
            if auth_redirect:
                return auth_redirect
            return self._handle_actor_request(actor_id, "properties", name=name)

        # Actor trust
        @self.flask_app.route("/<actor_id>/trust", methods=["GET", "POST", "DELETE", "PUT"])
        @self.flask_app.route("/<actor_id>/trust/<relationship>", methods=["GET", "POST", "DELETE", "PUT"])
        @self.flask_app.route("/<actor_id>/trust/<relationship>/<peerid>", methods=["GET", "POST", "DELETE", "PUT"])
        def app_trust(
            actor_id: str, relationship: Optional[str] = None, peerid: Optional[str] = None
        ) -> Union[Response, WerkzeugResponse, str]:
            return self._handle_actor_request(actor_id, "trust", relationship=relationship, peerid=peerid)

        # Trust permission management endpoints
        @self.flask_app.route("/<actor_id>/trust/<relationship>/<peerid>/permissions", methods=["GET", "PUT", "DELETE"])
        def app_trust_permissions(
            actor_id: str, relationship: str, peerid: str
        ) -> Union[Response, WerkzeugResponse, str]:
            return self._handle_actor_request(
                actor_id, "trust", relationship=relationship, peerid=peerid, permissions=True
            )

        # Actor subscriptions
        @self.flask_app.route("/<actor_id>/subscriptions", methods=["GET", "POST", "DELETE", "PUT"])
        @self.flask_app.route("/<actor_id>/subscriptions/<peerid>", methods=["GET", "POST", "DELETE", "PUT"])
        @self.flask_app.route("/<actor_id>/subscriptions/<peerid>/<subid>", methods=["GET", "POST", "DELETE", "PUT"])
        @self.flask_app.route("/<actor_id>/subscriptions/<peerid>/<subid>/<int:seqnr>", methods=["GET"])
        def app_subscriptions(
            actor_id: str, peerid: Optional[str] = None, subid: Optional[str] = None, seqnr: Optional[int] = None
        ) -> Union[Response, WerkzeugResponse, str]:
            return self._handle_actor_request(actor_id, "subscriptions", peerid=peerid, subid=subid, seqnr=seqnr)

        # Actor resources
        @self.flask_app.route("/<actor_id>/resources", methods=["GET", "POST", "DELETE", "PUT"])
        @self.flask_app.route("/<actor_id>/resources/<path:name>", methods=["GET", "POST", "DELETE", "PUT"])
        def app_resources(actor_id: str, name: str = "") -> Union[Response, WerkzeugResponse, str]:
            return self._handle_actor_request(actor_id, "resources", name=name)

        # Actor callbacks
        @self.flask_app.route("/<actor_id>/callbacks", methods=["GET", "POST", "DELETE", "PUT"])
        @self.flask_app.route("/<actor_id>/callbacks/<path:name>", methods=["GET", "POST", "DELETE", "PUT"])
        def app_callbacks(actor_id: str, name: str = "") -> Union[Response, WerkzeugResponse, str]:
            return self._handle_actor_request(actor_id, "callbacks", name=name)

        # Actor devtest
        @self.flask_app.route("/<actor_id>/devtest", methods=["GET", "POST", "DELETE", "PUT"])
        @self.flask_app.route("/<actor_id>/devtest/<path:path>", methods=["GET", "POST", "DELETE", "PUT"])
        def app_devtest(actor_id: str, path: str = "") -> Union[Response, WerkzeugResponse, str]:
            return self._handle_actor_request(actor_id, "devtest", path=path)

        # Actor methods
        @self.flask_app.route("/<actor_id>/methods", methods=["GET", "POST", "DELETE", "PUT"])
        @self.flask_app.route("/<actor_id>/methods/<path:name>", methods=["GET", "POST", "DELETE", "PUT"])
        def app_methods(actor_id: str, name: str = "") -> Union[Response, WerkzeugResponse, str]:
            return self._handle_actor_request(actor_id, "methods", name=name)

        # Actor actions
        @self.flask_app.route("/<actor_id>/actions", methods=["GET", "POST", "DELETE", "PUT"])
        @self.flask_app.route("/<actor_id>/actions/<path:name>", methods=["GET", "POST", "DELETE", "PUT"])
        def app_actions(actor_id: str, name: str = "") -> Union[Response, WerkzeugResponse, str]:
            return self._handle_actor_request(actor_id, "actions", name=name)

        # Third-party service OAuth2 callbacks and management
        @self.flask_app.route("/<actor_id>/services/<service_name>/callback", methods=["GET"])
        def app_services_callback(actor_id: str, service_name: str) -> Union[Response, WerkzeugResponse, str]:
            return self._handle_actor_request(actor_id, "services", name=service_name,
                                            code=request.args.get('code'),
                                            state=request.args.get('state'),
                                            error=request.args.get('error'))

        @self.flask_app.route("/<actor_id>/services/<service_name>", methods=["DELETE"])
        def app_services_revoke(actor_id: str, service_name: str) -> Union[Response, WerkzeugResponse, str]:
            return self._handle_actor_request(actor_id, "services", name=service_name)

    def _normalize_request(self) -> Dict[str, Any]:
        """Convert Flask request to ActingWeb format."""
        cookies = {}
        raw_cookies = request.headers.get("Cookie")
        if raw_cookies:
            for cookie in raw_cookies.split("; "):
                if "=" in cookie:
                    name, value = cookie.split("=", 1)
                    cookies[name] = value

        headers = {}
        for k, v in request.headers.items():
            headers[k] = v

        # If no Authorization header but we have an oauth_token cookie (web UI session),
        # provide it as a Bearer token so core auth can validate OAuth2 and authorize creator actions.
        if "Authorization" not in headers and cookies.get("oauth_token"):
            headers["Authorization"] = f"Bearer {cookies['oauth_token']}"

        params = {}
        for k, v in request.values.items():
            params[k] = v

        # Handle form data: Flask parses form-encoded bodies into request.form,
        # leaving request.data empty. Reconstruct the form-encoded body for OAuth2 handlers.
        data = request.data
        if not data and request.form:
            from urllib.parse import urlencode
            data = urlencode(request.form).encode('utf-8')

        return {
            "method": request.method,
            "path": request.path,
            "data": data,
            "headers": headers,
            "cookies": cookies,
            "values": params,
            "url": request.url,
        }

    def _create_flask_response(self, webobj: AWWebObj) -> Union[Response, WerkzeugResponse, str]:
        """Convert ActingWeb response to Flask response."""
        if webobj.response.redirect:
            response = redirect(webobj.response.redirect, code=302)
        else:
            response = Response(
                response=webobj.response.body,
                status=webobj.response.status_message,
                headers=webobj.response.headers,
            )

        response.status_code = webobj.response.status_code

        # Set cookies
        for cookie in webobj.response.cookies:
            response.set_cookie(
                cookie["name"],
                cookie["value"],
                max_age=cookie.get("max_age"),
                secure=cookie.get("secure", False),
                httponly=cookie.get("httponly", False),
            )

        return response

    def _handle_factory_request(self) -> Union[Response, WerkzeugResponse, str]:
        """Handle factory requests (actor creation)."""
        req_data = self._normalize_request()
        webobj = AWWebObj(
            url=req_data["url"],
            params=req_data["values"],
            body=req_data["data"],
            headers=req_data["headers"],
            cookies=req_data["cookies"],
        )

        # Check if user is already authenticated with OAuth2 and redirect to their actor
        oauth_cookie = request.cookies.get("oauth_token")
        if oauth_cookie and request.method == "GET":
            logging.debug(f"Processing GET request with OAuth cookie (length {len(oauth_cookie)})")
            # User has OAuth session - try to find their actor and redirect
            try:
                from ...oauth2 import create_oauth2_authenticator

                authenticator = create_oauth2_authenticator(self.aw_app.get_config())
                if authenticator.is_enabled():
                    logging.debug("OAuth2 is enabled, validating token...")
                    # Validate the token and get user info
                    user_info = authenticator.validate_token_and_get_user_info(oauth_cookie)
                    if user_info:
                        email = authenticator.get_email_from_user_info(user_info, oauth_cookie)
                        if email:
                            logging.debug(f"Token validation successful for {email}")
                            # Look up actor by email
                            actor_instance = authenticator.lookup_or_create_actor_by_email(email)
                            if actor_instance and actor_instance.id:
                                # Redirect to actor's www page
                                redirect_url = f"/{actor_instance.id}/www"
                                logging.debug(f"Redirecting authenticated user {email} to {redirect_url}")
                                return redirect(redirect_url, code=302)
                    # Token is invalid/expired - clear the cookie and redirect to new OAuth flow
                    logging.debug("OAuth token expired or invalid - clearing cookie and redirecting to OAuth")
                    original_url = request.url
                    oauth_redirect = self._create_oauth_redirect_response(
                        redirect_after_auth=original_url, clear_cookie=True
                    )
                    return oauth_redirect
                else:
                    logging.warning("OAuth2 not enabled in config")
            except Exception as e:
                logging.error(f"OAuth token validation failed in factory: {e}")
                # Token validation failed - clear cookie and redirect to fresh OAuth
                logging.debug("OAuth token validation error - clearing cookie and redirecting to OAuth")
                original_url = request.url
                oauth_redirect = self._create_oauth_redirect_response(
                    redirect_after_auth=original_url, clear_cookie=True
                )
                return oauth_redirect

        # Use the standard factory handler
        handler = factory.RootFactoryHandler(webobj, self.aw_app.get_config(), hooks=self.aw_app.hooks)

        try:
            method_name = request.method.lower()
            handler_method = getattr(handler, method_name, None)
            if handler_method and callable(handler_method):
                handler_method()
            else:
                return Response(status=405)
        except Exception as e:
            logging.error(f"Error in factory handler: {e}")
            # Map common network/SSL errors to clearer status codes if handler didn't set one
            if webobj.response.status_code != 200:
                pass
            else:
                error_message = str(e).lower()
                if "ssl" in error_message or "certificate" in error_message:
                    webobj.response.set_status(502, "Bad Gateway - SSL connection failed")
                elif "connection" in error_message or "timeout" in error_message:
                    webobj.response.set_status(503, "Service Unavailable - Connection failed")
                else:
                    webobj.response.set_status(500, "Internal server error")
            return self._create_flask_response(webobj)

        # Handle template rendering for factory
        if request.method == "GET" and webobj.response.status_code == 200:
            try:
                return Response(render_template("aw-root-factory.html", **webobj.response.template_values))
            except Exception:
                pass  # Fall back to default response
        elif request.method == "POST":
            # Only render templates for form submissions, not JSON requests
            is_json_request = request.content_type and "application/json" in request.content_type
            if not is_json_request and webobj.response.status_code in [200, 201]:
                try:
                    return Response(render_template("aw-root-created.html", **webobj.response.template_values))
                except Exception:
                    pass  # Fall back to default response
            elif not is_json_request and webobj.response.status_code == 400:
                try:
                    return Response(render_template("aw-root-failed.html", **webobj.response.template_values))
                except Exception:
                    pass  # Fall back to default response

        return self._create_flask_response(webobj)

    def _handle_factory_get_request(self) -> Union[Response, WerkzeugResponse, str]:
        """Handle GET requests to factory route - just show the email form."""
        # Simply show the factory template without any authentication
        try:
            return Response(render_template("aw-root-factory.html"))
        except Exception:
            # Fallback for when templates are not available
            return Response(
                """
                <html>
                <head><title>ActingWeb Demo</title></head>
                <body>
                    <h1>Welcome to ActingWeb Demo</h1>
                    <form action="/" method="post">
                        <label>Your Email: <input type="email" name="creator" required /></label>
                        <input type="submit" value="Create Actor" />
                    </form>
                </body>
                </html>
            """,
                mimetype="text/html",
            )

    def _handle_factory_post_with_oauth_redirect(self) -> Union[Response, WerkzeugResponse, str]:
        """Handle POST to factory route with OAuth2 redirect including email hint."""
        try:
            import json

            # Parse the form data to extract email
            req_data = self._normalize_request()
            email = None

            # Try to get email from JSON body first
            if req_data["data"]:
                try:
                    data = json.loads(req_data["data"])
                    email = data.get("creator") or data.get("email")
                except (json.JSONDecodeError, ValueError):
                    pass

            # Fallback to form data
            if not email:
                email = req_data["values"].get("creator") or req_data["values"].get("email")

            if not email:
                # No email provided - return error or redirect back to form
                try:
                    return Response(render_template("aw-root-factory.html", error="Email is required"))
                except Exception:
                    return Response("Email is required", status=400)

            logging.debug(f"Factory POST with email: {email}")

            # Create OAuth2 redirect with email hint
            try:
                from ...oauth2 import create_oauth2_authenticator

                authenticator = create_oauth2_authenticator(self.aw_app.get_config())
                if authenticator.is_enabled():
                    # Create authorization URL with email hint and User-Agent
                    redirect_after_auth = request.url  # Redirect back to factory after auth
                    user_agent = request.headers.get("User-Agent", "")
                    auth_url = authenticator.create_authorization_url(
                        redirect_after_auth=redirect_after_auth, email_hint=email, user_agent=user_agent
                    )

                    logging.debug(f"Redirecting to OAuth2 with email hint: {email}")
                    return redirect(auth_url)
                else:
                    logging.warning("OAuth2 not configured - falling back to standard actor creation")
                    # Fall back to standard actor creation without OAuth
                    return self._handle_factory_post_without_oauth(email)

            except Exception as e:
                logging.error(f"Error creating OAuth2 redirect: {e}")
                # Fall back to standard actor creation if OAuth2 setup fails
                logging.debug("OAuth2 setup failed - falling back to standard actor creation")
                return self._handle_factory_post_without_oauth(email)

        except Exception as e:
            logging.error(f"Error in factory POST handler: {e}")
            return Response("Internal server error", status=500)

    def _handle_factory_post_without_oauth(self, email: str) -> Union[Response, WerkzeugResponse, str]:  # pylint: disable=unused-argument
        """Handle POST to factory route without OAuth2 - standard actor creation."""
        try:
            # Always use the standard factory handler
            req_data = self._normalize_request()
            webobj = AWWebObj(
                url=req_data["url"],
                params=req_data["values"],
                body=req_data["data"],
                headers=req_data["headers"],
                cookies=req_data["cookies"],
            )

            # Use the standard factory handler
            handler = factory.RootFactoryHandler(webobj, self.aw_app.get_config(), hooks=self.aw_app.hooks)
            handler.post()

            # Handle template rendering for factory
            if webobj.response.status_code in [200, 201]:
                try:
                    return Response(render_template("aw-root-created.html", **webobj.response.template_values))
                except Exception:
                    pass  # Fall back to default response
            elif webobj.response.status_code == 400:
                try:
                    return Response(render_template("aw-root-failed.html", **webobj.response.template_values))
                except Exception:
                    pass  # Fall back to default response

            return self._create_flask_response(webobj)

        except Exception as e:
            logging.error(f"Error in standard actor creation: {e}")
            try:
                return Response(render_template("aw-root-failed.html", error="Actor creation failed"))
            except Exception:
                return Response("Actor creation failed", status=500)

    def _handle_bot_request(self) -> Union[Response, WerkzeugResponse, str]:
        """Handle bot requests."""
        req_data = self._normalize_request()
        webobj = AWWebObj(
            url=req_data["url"],
            params=req_data["values"],
            body=req_data["data"],
            headers=req_data["headers"],
            cookies=req_data["cookies"],
        )

        handler = bot.BotHandler(webobj=webobj, config=self.aw_app.get_config(), hooks=self.aw_app.hooks)
        handler.post(path="/bot")

        return self._create_flask_response(webobj)

    def _handle_oauth2_callback(self) -> Union[Response, WerkzeugResponse, str]:
        """Handle OAuth2 callback."""
        req_data = self._normalize_request()
        webobj = AWWebObj(
            url=req_data["url"],
            params=req_data["values"],
            body=req_data["data"],
            headers=req_data["headers"],
            cookies=req_data["cookies"],
        )

        from ...handlers.oauth2_callback import OAuth2CallbackHandler

        handler = OAuth2CallbackHandler(webobj, self.aw_app.get_config(), hooks=self.aw_app.hooks)
        result = handler.get()

        # Handle OAuth2 errors with template rendering for better UX
        if isinstance(result, dict) and result.get("error") and webobj.response.status_code >= 400:
            if webobj.response.template_values:
                try:
                    return Response(render_template("aw-root-failed.html", **webobj.response.template_values))
                except Exception:
                    pass  # Fall back to default response

        return self._create_flask_response(webobj)

    def _handle_oauth2_endpoint(self, endpoint: str) -> Union[Response, WerkzeugResponse, str]:
        """Handle OAuth2 endpoints (register, authorize, token)."""
        req_data = self._normalize_request()
        webobj = AWWebObj(
            url=req_data["url"],
            params=req_data["values"],
            body=req_data["data"],
            headers=req_data["headers"],
            cookies=req_data["cookies"],
        )

        from ...handlers.oauth2_endpoints import OAuth2EndpointsHandler

        handler = OAuth2EndpointsHandler(webobj, self.aw_app.get_config(), hooks=self.aw_app.hooks)

        if request.method == "POST":
            result = handler.post(endpoint)
        elif request.method == "OPTIONS":
            result = handler.options(endpoint)
        else:
            result = handler.get(endpoint)

        # Check if handler set template values (for HTML response)
        if hasattr(webobj.response, "template_values") and webobj.response.template_values:
            # This is an HTML template response
            template_name = "aw-oauth-authorization-form.html"  # Default OAuth2 template
            try:
                return Response(render_template(template_name, **webobj.response.template_values))
            except Exception as e:
                # Template not found or rendering error - fall back to JSON
                from flask import jsonify

                return jsonify(
                    {
                        "error": "template_error",
                        "error_description": f"Failed to render template: {str(e)}",
                        "template_values": webobj.response.template_values,
                    }
                )

        # Handle redirect responses (e.g., OAuth2 callbacks)
        if isinstance(result, dict) and result.get("status") == "redirect":
            redirect_url = result.get("location")
            if redirect_url:
                redirect_response = redirect(redirect_url, code=302)
                
                # Add CORS headers for OAuth2 redirect responses  
                redirect_response.headers["Access-Control-Allow-Origin"] = "*"
                redirect_response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
                redirect_response.headers["Access-Control-Allow-Headers"] = "Authorization, Content-Type, mcp-protocol-version"
                
                return redirect_response

        # Return the OAuth2 result as JSON with CORS headers
        from flask import jsonify

        json_response = jsonify(result)

        # Use the status code from the handler if set
        if hasattr(webobj.response, 'status_code') and webobj.response.status_code:
            json_response.status_code = webobj.response.status_code

        # Add CORS headers for OAuth2 endpoints
        json_response.headers["Access-Control-Allow-Origin"] = "*"
        json_response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        json_response.headers["Access-Control-Allow-Headers"] = "Authorization, Content-Type, mcp-protocol-version"
        json_response.headers["Access-Control-Max-Age"] = "86400"

        return json_response

    def _handle_oauth2_discovery_endpoint(self, endpoint: str) -> Union[Response, WerkzeugResponse, str]:
        """Handle OAuth2 discovery endpoints that return JSON directly."""
        req_data = self._normalize_request()
        webobj = AWWebObj(
            url=req_data["url"],
            params=req_data["values"],
            body=req_data["data"],
            headers=req_data["headers"],
            cookies=req_data["cookies"],
        )

        from ...handlers.oauth2_endpoints import OAuth2EndpointsHandler

        handler = OAuth2EndpointsHandler(webobj, self.aw_app.get_config(), hooks=self.aw_app.hooks)

        if request.method == "OPTIONS":
            result = handler.options(endpoint)
        else:
            result = handler.get(endpoint)

        # Add CORS headers directly for OAuth2 discovery endpoints
        from flask import jsonify

        response = jsonify(result)
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Authorization, Content-Type, mcp-protocol-version"
        response.headers["Access-Control-Max-Age"] = "86400"

        return response

    def _handle_mcp_request(self) -> Union[Response, WerkzeugResponse, str]:
        """Handle MCP requests."""
        req_data = self._normalize_request()
        webobj = AWWebObj(
            url=req_data["url"],
            params=req_data["values"],
            body=req_data["data"],
            headers=req_data["headers"],
            cookies=req_data["cookies"],
        )

        handler = mcp.MCPHandler(webobj, self.aw_app.get_config(), hooks=self.aw_app.hooks)

        # Execute appropriate method based on request method
        if request.method == "GET":
            result = handler.get()
        elif request.method == "POST":
            import json

            # Parse JSON body for POST requests
            try:
                if webobj.request.body:
                    data = json.loads(webobj.request.body)
                else:
                    data = {}
            except (json.JSONDecodeError, ValueError):
                data = {}

            result = handler.post(data)
        else:
            return Response(status=405)

        # Create JSON response
        from flask import jsonify

        return jsonify(result)

    def _check_authentication_and_redirect(self) -> Optional[Union[Response, WerkzeugResponse, str]]:
        """Check if request is authenticated, if not return OAuth2 redirect."""
        # Check for Basic auth
        auth_header = request.headers.get("Authorization")
        if auth_header and auth_header.startswith("Basic "):
            return None  # Has basic auth, let normal flow handle it

        # Check for Bearer token
        if auth_header and auth_header.startswith("Bearer "):
            # Align with FastAPI: if a Bearer token is present, let the underlying handlers verify it.
            # This supports both OAuth2 tokens and ActingWeb trust secret tokens without forcing redirect here.
            return None

        # Check for OAuth token cookie (for session-based authentication)
        oauth_cookie = request.cookies.get("oauth_token")
        if oauth_cookie:
            logging.debug(f"Found oauth_token cookie with length {len(oauth_cookie)}")
            # Validate the OAuth cookie token
            try:
                from ...oauth2 import create_oauth2_authenticator

                authenticator = create_oauth2_authenticator(self.aw_app.get_config())
                if authenticator.is_enabled():
                    user_info = authenticator.validate_token_and_get_user_info(oauth_cookie)
                    if user_info:
                        email = authenticator.get_email_from_user_info(user_info, oauth_cookie)
                        if email:
                            logging.debug(f"OAuth cookie validation successful for {email}")
                            return None  # Valid OAuth cookie
                    logging.debug("OAuth cookie token is expired or invalid - will redirect to fresh OAuth")
            except Exception as e:
                logging.debug(f"OAuth cookie validation error: {e} - will redirect to fresh OAuth")

        # No valid authentication - redirect to OAuth2
        original_url = request.url
        return self._create_oauth_redirect_response(redirect_after_auth=original_url, clear_cookie=bool(oauth_cookie))

    def _create_oauth_redirect_response(
        self, redirect_after_auth: str = "", clear_cookie: bool = False
    ) -> Union[Response, WerkzeugResponse, str]:
        """Create OAuth2 redirect response."""
        try:
            from ...oauth2 import create_oauth2_authenticator

            authenticator = create_oauth2_authenticator(self.aw_app.get_config())
            if authenticator.is_enabled():
                auth_url = authenticator.create_authorization_url(redirect_after_auth=redirect_after_auth)
                if auth_url:
                    response = redirect(auth_url, code=302)
                    if clear_cookie:
                        # Clear the expired oauth_token cookie
                        response.delete_cookie("oauth_token", path="/")
                        logging.debug("Cleared expired oauth_token cookie")
                    return response
        except Exception as e:
            logging.error(f"Error creating OAuth2 redirect: {e}")

        # Fallback to 401 if OAuth2 not configured
        response = Response("Authentication required", status=401)
        response.headers["WWW-Authenticate"] = 'Bearer realm="ActingWeb"'
        return response

    def _handle_actor_request(
        self, actor_id: str, endpoint: str, **kwargs: Any
    ) -> Union[Response, WerkzeugResponse, str]:
        """Handle actor-specific requests."""
        req_data = self._normalize_request()
        webobj = AWWebObj(
            url=req_data["url"],
            params=req_data["values"],
            body=req_data["data"],
            headers=req_data["headers"],
            cookies=req_data["cookies"],
        )

        # Get appropriate handler
        handler = self._get_handler(endpoint, webobj, actor_id, **kwargs)
        if not handler:
            return Response(status=404)

        # Execute handler method
        try:
            method_name = request.method.lower()
            handler_method = getattr(handler, method_name, None)
            if handler_method and callable(handler_method):
                # Build positional arguments based on endpoint and kwargs
                args = [actor_id]
                if endpoint == "meta":
                    # MetaHandler.get(actor_id, path) - path defaults to "" if not provided
                    args.append(kwargs.get("path", ""))
                elif endpoint == "trust":
                    if kwargs.get("relationship"):
                        args.append(kwargs["relationship"])
                    if kwargs.get("peerid"):
                        args.append(kwargs["peerid"])
                elif endpoint == "subscriptions":
                    # Different subscription handlers:
                    # SubscriptionRootHandler.get(actor_id)
                    # SubscriptionRelationshipHandler.get(actor_id, peerid)
                    # SubscriptionHandler.get(actor_id, peerid, subid)
                    # SubscriptionDiffHandler.get(actor_id, peerid, subid, seqnr)
                    if kwargs.get("peerid"):
                        args.append(kwargs["peerid"])
                    if kwargs.get("subid"):
                        args.append(kwargs["subid"])
                    if kwargs.get("seqnr"):
                        args.append(kwargs["seqnr"])
                elif endpoint == "www":
                    # WwwHandler.get(actor_id, path) - path defaults to "" if not provided
                    args.append(kwargs.get("path", ""))
                elif endpoint == "properties":
                    # PropertiesHandler.get(actor_id, name) - name defaults to "" if not provided
                    args.append(kwargs.get("name", ""))
                elif endpoint == "callbacks":
                    # CallbacksHandler.get(actor_id, name) - name defaults to "" if not provided
                    args.append(kwargs.get("name", ""))
                elif endpoint == "resources":
                    # ResourcesHandler.get(actor_id, name) - name defaults to "" if not provided
                    args.append(kwargs.get("name", ""))
                elif endpoint == "devtest":
                    # DevtestHandler.get(actor_id, path) - path defaults to "" if not provided
                    args.append(kwargs.get("path", ""))
                elif endpoint == "methods":
                    # MethodsHandler.get(actor_id, name) - name defaults to "" if not provided
                    args.append(kwargs.get("name", ""))
                elif endpoint == "actions":
                    # ActionsHandler.get(actor_id, name) - name defaults to "" if not provided
                    args.append(kwargs.get("name", ""))
                elif endpoint == "services":
                    # ServicesHandler.get(actor_id, service_name, **kwargs) - service_name from name parameter
                    service_name = kwargs.get("name", "")
                    args.append(service_name)
                    # For services, we need to pass additional kwargs (code, state, error)
                    for key in ["code", "state", "error"]:
                        if key in kwargs:
                            kwargs[key] = kwargs[key]

                handler_method(*args, **{k: v for k, v in kwargs.items() if k in ["code", "state", "error"]})
            else:
                return Response(status=405)
        except Exception as e:
            logging.error(f"Error in {endpoint} handler: {e}")
            # Map common network/SSL errors to clearer status codes if handler didn't set one
            if webobj.response.status_code != 200:
                pass
            else:
                error_message = str(e).lower()
                if "ssl" in error_message or "certificate" in error_message:
                    webobj.response.set_status(502, "Bad Gateway - SSL connection failed")
                elif "connection" in error_message or "timeout" in error_message:
                    webobj.response.set_status(503, "Service Unavailable - Connection failed")
                else:
                    webobj.response.set_status(500, "Internal server error")
            return self._create_flask_response(webobj)

        # Special handling for www endpoint templates
        if endpoint == "www" and request.method == "GET" and webobj.response.status_code == 200:
            path = kwargs.get("path", "")
            template_values = webobj.response.template_values or {}
            try:
                if not path:
                    return Response(render_template("aw-actor-www-root.html", **template_values))
                elif path == "init":
                    return Response(render_template("aw-actor-www-init.html", **template_values))
                elif path == "properties":
                    return Response(render_template("aw-actor-www-properties.html", **template_values))
                elif path == "property":
                    return Response(render_template("aw-actor-www-property.html", **template_values))
                elif path == "trust/new":
                    return Response(render_template("aw-actor-www-trust-new.html", **template_values))
                elif path.startswith("properties/"):
                    # Handle individual property pages like "properties/notes", "properties/demo_version"
                    return Response(render_template("aw-actor-www-property.html", **template_values))
                elif path == "trust":
                    return Response(render_template("aw-actor-www-trust.html", **template_values))
            except Exception:
                pass  # Fall back to default response

        return self._create_flask_response(webobj)

    def _get_handler(
        self, endpoint: str, webobj: AWWebObj, actor_id: str, **kwargs: Any  # pylint: disable=unused-argument
    ) -> Optional[Any]:
        """Get the appropriate handler for an endpoint."""
        config = self.aw_app.get_config()

        handlers = {
            "root": lambda: root.RootHandler(webobj, config, hooks=self.aw_app.hooks),
            "meta": lambda: meta.MetaHandler(webobj, config, hooks=self.aw_app.hooks),
            "www": lambda: www.WwwHandler(webobj, config, hooks=self.aw_app.hooks),
            "properties": lambda: properties.PropertiesHandler(webobj, config, hooks=self.aw_app.hooks),
            "resources": lambda: resources.ResourcesHandler(webobj, config, hooks=self.aw_app.hooks),
            "callbacks": lambda: callbacks.CallbacksHandler(webobj, config, hooks=self.aw_app.hooks),
            "devtest": lambda: devtest.DevtestHandler(webobj, config, hooks=self.aw_app.hooks),
            "methods": lambda: methods.MethodsHandler(webobj, config, hooks=self.aw_app.hooks),
            "actions": lambda: actions.ActionsHandler(webobj, config, hooks=self.aw_app.hooks),
            "services": lambda: self._create_services_handler(webobj, config),
        }

        # Special handling for trust endpoint
        if endpoint == "trust":
            relationship = kwargs.get("relationship")
            peerid = kwargs.get("peerid")
            
            # Check for permissions endpoint
            if kwargs.get("permissions"):
                return trust.TrustPermissionHandler(webobj, config, hooks=self.aw_app.hooks)
            
            # For trust endpoint, we need to distinguish between path parameters and query parameters
            # If peerid appears in query params but not as path param, it's a query-based request
            query_peerid = webobj.request.get("peerid")
            
            # Only count actual path parameters (non-None, non-empty)
            path_parts = []
            if relationship is not None and relationship != "":
                path_parts.append(relationship)
            # Only count peerid as path param if it's not a query param request
            if peerid is not None and peerid != "" and not query_peerid:
                path_parts.append(peerid)
            
            if len(path_parts) == 0:
                return trust.TrustHandler(webobj, config, hooks=self.aw_app.hooks)
            elif len(path_parts) == 1:
                return trust.TrustRelationshipHandler(webobj, config, hooks=self.aw_app.hooks)
            else:
                return trust.TrustPeerHandler(webobj, config, hooks=self.aw_app.hooks)

        # Special handling for subscriptions endpoint
        if endpoint == "subscriptions":
            path_parts = [p for p in [kwargs.get("peerid"), kwargs.get("subid")] if p]
            seqnr = kwargs.get("seqnr")

            if len(path_parts) == 0:
                return subscription.SubscriptionRootHandler(webobj, config, hooks=self.aw_app.hooks)
            elif len(path_parts) == 1:
                return subscription.SubscriptionRelationshipHandler(webobj, config, hooks=self.aw_app.hooks)
            elif len(path_parts) == 2 and seqnr is None:
                return subscription.SubscriptionHandler(webobj, config, hooks=self.aw_app.hooks)
            else:
                return subscription.SubscriptionDiffHandler(webobj, config, hooks=self.aw_app.hooks)

        if endpoint in handlers:
            return handlers[endpoint]()

        return None

    def _create_oauth_discovery_response(self) -> Dict[str, Any]:
        """Create OAuth2 Authorization Server Discovery response (RFC 8414)."""
        config = self.aw_app.get_config()
        base_url = f"{config.proto}{config.fqdn}"
        oauth_provider = getattr(config, "oauth2_provider", "google")

        if oauth_provider == "google":
            return {
                "issuer": base_url,
                "authorization_endpoint": "https://accounts.google.com/o/oauth2/v2/auth",
                "token_endpoint": "https://oauth2.googleapis.com/token",
                "userinfo_endpoint": "https://www.googleapis.com/oauth2/v2/userinfo",
                "jwks_uri": "https://www.googleapis.com/oauth2/v3/certs",
                "scopes_supported": ["openid", "email", "profile"],
                "response_types_supported": ["code"],
                "grant_types_supported": ["authorization_code", "refresh_token"],
                "subject_types_supported": ["public"],
                "id_token_signing_alg_values_supported": ["RS256"],
                "code_challenge_methods_supported": ["S256"],
                "token_endpoint_auth_methods_supported": ["client_secret_post", "client_secret_basic"],
            }
        elif oauth_provider == "github":
            return {
                "issuer": base_url,
                "authorization_endpoint": "https://github.com/login/oauth/authorize",
                "token_endpoint": "https://github.com/login/oauth/access_token",
                "userinfo_endpoint": "https://api.github.com/user",
                "scopes_supported": ["user:email"],
                "response_types_supported": ["code"],
                "grant_types_supported": ["authorization_code"],
                "subject_types_supported": ["public"],
                "token_endpoint_auth_methods_supported": ["client_secret_post", "client_secret_basic"],
            }
        else:
            return {"error": "Unknown OAuth provider"}

    def _create_mcp_info_response(self) -> Dict[str, Any]:
        """Create MCP information response."""
        config = self.aw_app.get_config()
        base_url = f"{config.proto}{config.fqdn}"
        oauth_provider = getattr(config, "oauth2_provider", "google")

        return {
            "mcp_enabled": True,
            "mcp_endpoint": "/mcp",
            "authentication": {
                "type": "oauth2",
                "provider": "actingweb",
                "required_scopes": ["mcp"],
                "flow": "authorization_code",
                "auth_url": f"{base_url}/oauth/authorize",
                "token_url": f"{base_url}/oauth/token",
                "callback_url": f"{base_url}/oauth/callback",
                "registration_endpoint": f"{base_url}/oauth/register",
                "authorization_endpoint": f"{base_url}/oauth/authorize",
                "token_endpoint": f"{base_url}/oauth/token",
                "discovery_url": f"{base_url}/.well-known/oauth-authorization-server",
                "resource_discovery_url": f"{base_url}/.well-known/oauth-protected-resource",
                "enabled": True,
            },
            "supported_features": ["tools", "prompts"],
            "tools_count": 4,  # search, fetch, create_note, create_reminder
            "prompts_count": 3,  # analyze_notes, create_learning_prompt, create_meeting_prep
            "actor_lookup": "email_based",
            "description": f"ActingWeb MCP Demo - AI can interact with actors through MCP protocol using {oauth_provider.title()} OAuth2",
        }

    def _create_services_handler(self, webobj: AWWebObj, config) -> Any:
        """Create services handler with service registry injection."""
        handler = services.ServicesHandler(webobj, config, hooks=self.aw_app.hooks)
        # Inject service registry into the handler so it can access it
        handler._service_registry = self.aw_app.get_service_registry()
        return handler
