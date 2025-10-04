import logging
import os

from pynamodb.attributes import BooleanAttribute, UnicodeAttribute, UTCDateTimeAttribute
from pynamodb.indexes import AllProjection, GlobalSecondaryIndex
from pynamodb.models import Model
from datetime import datetime

"""
    DbTrust handles all db operations for a trust
    Google datastore for google is used as a backend.
"""


class SecretIndex(GlobalSecondaryIndex):
    """
    Secondary index on trust
    """

    class Meta:
        index_name = "secret-index"
        read_capacity_units = 2
        write_capacity_units = 1
        projection = AllProjection()

    secret = UnicodeAttribute(hash_key=True)


class Trust(Model):
    """Data model for a trust relationship"""

    class Meta:  # type: ignore[misc]
        table_name = os.getenv("AWS_DB_PREFIX", "demo_actingweb") + "_trusts"
        read_capacity_units = 5
        write_capacity_units = 2
        region = os.getenv("AWS_DEFAULT_REGION", "us-west-1")
        host = os.getenv("AWS_DB_HOST", None)

    # Existing attributes
    id = UnicodeAttribute(hash_key=True)  # actor_id
    peerid = UnicodeAttribute(range_key=True)
    baseuri = UnicodeAttribute()
    type = UnicodeAttribute()  # peer's ActingWeb mini-application type (e.g., "urn:actingweb:example.com:banking")
    relationship = UnicodeAttribute()  # trust type (e.g., "friend", "admin", "partner") - defines permission level
    secret = UnicodeAttribute()
    desc = UnicodeAttribute()
    approved = BooleanAttribute()
    peer_approved = BooleanAttribute()
    verified = BooleanAttribute()
    verification_token = UnicodeAttribute()

    # New attributes for unified trust system
    peer_identifier = UnicodeAttribute(null=True)  # Email, username, UUID - service-specific identifier
    established_via = UnicodeAttribute(null=True)  # 'actingweb', 'oauth2_interactive', 'oauth2_client'
    created_at = UTCDateTimeAttribute(null=True)  # When trust was created
    last_accessed = UTCDateTimeAttribute(null=True)  # Last time trust was used

    # Client metadata for OAuth2 clients (MCP, etc.)
    client_name = UnicodeAttribute(null=True)  # Friendly name of the client (e.g., "ChatGPT", "Claude", "MCP Inspector")
    client_version = UnicodeAttribute(null=True)  # Version of the client software
    client_platform = UnicodeAttribute(null=True)  # Platform info from User-Agent
    oauth_client_id = UnicodeAttribute(null=True)  # Reference to OAuth2 client ID for credentials-based clients

    # Indexes
    secret_index = SecretIndex()


class DbTrust:
    """
    DbTrust does all the db operations for trust objects

    The  actor_id must always be set.
    """

    def get(self, actor_id=None, peerid=None, token=None):
        """Retrieves the trust from the database

        Either peerid or token must be set.
        If peerid is set, token will be ignored.
        """
        if not actor_id:
            return None
        try:
            if not self.handle and peerid:
                logging.debug("    Retrieving trust from db based on peerid(" + peerid + ")")
                self.handle = Trust.get(actor_id, peerid, consistent_read=True)
            elif not self.handle and token:
                logging.debug("    Retrieving trust from db based on token(" + token + ")")
                res = Trust.secret_index.query(token)
                for h in res:
                    if actor_id == h.id:
                        self.handle = h
                        break
        except Exception:  # PynamoDB DoesNotExist exception
            return None
        if not self.handle:
            return None
        t = self.handle
        result = {
            "id": t.id,
            "peerid": t.peerid,
            "baseuri": t.baseuri,
            "type": t.type,
            "relationship": t.relationship,
            "secret": t.secret,
            "desc": t.desc,
            "approved": t.approved,
            "peer_approved": t.peer_approved,
            "verified": t.verified,
            "verification_token": t.verification_token,
        }

        # Add new unified trust attributes if they exist
        if hasattr(t, "peer_identifier") and t.peer_identifier:
            result["peer_identifier"] = t.peer_identifier
        if hasattr(t, "established_via") and t.established_via:
            result["established_via"] = t.established_via
        if hasattr(t, "created_at") and t.created_at:
            result["created_at"] = t.created_at.isoformat() if t.created_at else None
        if hasattr(t, "last_accessed") and t.last_accessed:
            result["last_accessed"] = t.last_accessed.isoformat() if t.last_accessed else None

        # Add client metadata for OAuth2 clients if they exist
        if hasattr(t, "client_name") and t.client_name:
            result["client_name"] = t.client_name
        if hasattr(t, "client_version") and t.client_version:
            result["client_version"] = t.client_version
        if hasattr(t, "client_platform") and t.client_platform:
            result["client_platform"] = t.client_platform
        if hasattr(t, "oauth_client_id") and t.oauth_client_id:
            result["oauth_client_id"] = t.oauth_client_id

        return result

    def modify(
        self,
        baseuri=None,
        secret=None,
        desc=None,
        approved=None,
        verified=None,
        verification_token=None,
        peer_approved=None,
        # New unified trust attributes
        peer_identifier=None,
        established_via=None,
        last_accessed=None,
        # Client metadata for OAuth2 clients
        client_name=None,
        client_version=None,
        client_platform=None,
        oauth_client_id=None,
    ):
        """Modify a trust

        If bools are none, they will not be changed.
        """
        if not self.handle:
            logging.debug("Attempted modification of DbTrust without db handle")
            return False
        if baseuri and len(baseuri) > 0:
            self.handle.baseuri = baseuri
        if secret and len(secret) > 0:
            self.handle.secret = secret
        if desc and len(desc) > 0:
            self.handle.desc = desc
        if approved is not None:
            self.handle.approved = approved
        if verified is not None:
            self.handle.verified = verified
        if verification_token and len(verification_token) > 0:
            self.handle.verification_token = verification_token
        if peer_approved is not None:
            self.handle.peer_approved = peer_approved

        # Handle new unified trust attributes
        if peer_identifier is not None:
            self.handle.peer_identifier = peer_identifier
        if established_via is not None:
            self.handle.established_via = established_via
        if last_accessed is not None:
            if isinstance(last_accessed, str):
                from datetime import datetime

                self.handle.last_accessed = datetime.fromisoformat(last_accessed.replace("Z", "+00:00"))
            else:
                self.handle.last_accessed = last_accessed

        # Handle client metadata for OAuth2 clients
        if client_name is not None:
            self.handle.client_name = client_name
        if client_version is not None:
            self.handle.client_version = client_version
        if client_platform is not None:
            self.handle.client_platform = client_platform
        if oauth_client_id is not None:
            self.handle.oauth_client_id = oauth_client_id

        self.handle.save()
        return True

    def create(
        self,
        actor_id=None,
        peerid=None,
        baseuri="",
        peer_type="",
        relationship="",
        secret="",
        approved="",
        verified=False,
        peer_approved=False,
        verification_token="",
        desc="",
        # New unified trust attributes
        peer_identifier=None,
        established_via=None,
        # Client metadata for OAuth2 clients
        client_name=None,
        client_version=None,
        client_platform=None,
        oauth_client_id=None,
    ):
        """Create a new trust"""
        if not actor_id or not peerid:
            return False
        from datetime import datetime

        # Create trust with existing attributes
        trust_kwargs = {
            "id": actor_id,
            "peerid": peerid,
            "baseuri": baseuri,
            "type": peer_type,
            "relationship": relationship,
            "secret": secret,
            "approved": approved,
            "verified": verified,
            "peer_approved": peer_approved,
            "verification_token": verification_token,
            "desc": desc,
        }

        # Add new unified trust attributes if provided
        if peer_identifier is not None:
            trust_kwargs["peer_identifier"] = peer_identifier
        if established_via is not None:
            trust_kwargs["established_via"] = established_via

        # Add client metadata if provided
        if client_name is not None:
            trust_kwargs["client_name"] = client_name
        if client_version is not None:
            trust_kwargs["client_version"] = client_version
        if client_platform is not None:
            trust_kwargs["client_platform"] = client_platform
        if oauth_client_id is not None:
            trust_kwargs["oauth_client_id"] = oauth_client_id

        # Always set created_at for new trusts
        trust_kwargs["created_at"] = datetime.utcnow()

        self.handle = Trust(**trust_kwargs)
        self.handle.save()
        return True

    def delete(self):
        """Deletes the property in the database"""
        if not self.handle:
            return False
        self.handle.delete()
        self.handle = None
        return True

    @staticmethod
    def is_token_in_db(actor_id=None, token=None):
        """Returns True if token is found in db"""
        if not actor_id or len(actor_id) == 0:
            return False
        if not token or len(token) == 0:
            return False
        for r in Trust.secret_index.query(token):
            if r.id != actor_id:
                continue
            else:
                return True
        return False

    def __init__(self):
        self.handle = None
        if not Trust.exists():
            Trust.create_table(wait=True)


class DbTrustList:
    """
    DbTrustList does all the db operations for list of trust objects

    The  actor_id must always be set.
    """

    def fetch(self, actor_id):
        """Retrieves the trusts of an actor_id from the database as an array"""
        if not actor_id:
            return None
        self.actor_id = actor_id
        self.handle = Trust.scan(Trust.id == self.actor_id, consistent_read=True)
        self.trusts = []
        if self.handle:
            for t in self.handle:
                result = {
                    "id": t.id,
                    "peerid": t.peerid,
                    "baseuri": t.baseuri,
                    "type": t.type,
                    "relationship": t.relationship,
                    "secret": t.secret,
                    "desc": t.desc,
                    "approved": t.approved,
                    "peer_approved": t.peer_approved,
                    "verified": t.verified,
                    "verification_token": t.verification_token,
                }

                # Add new unified trust attributes if they exist (same logic as get() method)
                if hasattr(t, "peer_identifier") and t.peer_identifier:
                    result["peer_identifier"] = t.peer_identifier
                if hasattr(t, "established_via"):
                    result["established_via"] = t.established_via
                if hasattr(t, "created_at") and t.created_at:
                    result["created_at"] = t.created_at.isoformat() if t.created_at else None
                if hasattr(t, "last_accessed") and t.last_accessed:
                    result["last_accessed"] = t.last_accessed.isoformat() if t.last_accessed else None

                # Add client metadata for OAuth2 clients if they exist (same logic as get() method)
                if hasattr(t, "client_name") and t.client_name:
                    result["client_name"] = t.client_name
                if hasattr(t, "client_version") and t.client_version:
                    result["client_version"] = t.client_version
                if hasattr(t, "client_platform") and t.client_platform:
                    result["client_platform"] = t.client_platform
                if hasattr(t, "oauth_client_id") and t.oauth_client_id:
                    result["oauth_client_id"] = t.oauth_client_id

                self.trusts.append(result)
            return self.trusts
        else:
            return []

    def delete(self):
        """Deletes all the properties in the database"""
        self.handle = Trust.scan(Trust.id == self.actor_id, consistent_read=True)
        if not self.handle:
            return False
        for p in self.handle:
            p.delete()
        self.handle = None
        return True

    def __init__(self):
        self.handle = None
        self.actor_id = None
        self.trusts = []
        if not Trust.exists():
            Trust.create_table(wait=True)
