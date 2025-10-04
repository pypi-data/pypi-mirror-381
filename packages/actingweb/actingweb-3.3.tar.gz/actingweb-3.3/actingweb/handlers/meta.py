import json

from actingweb import auth
from actingweb.handlers import base_handler


class MetaHandler(base_handler.BaseHandler):

    def get(self, actor_id, path):
        # Meta endpoint allows unauthenticated access but still needs actor data
        myself = self.get_actor_allow_unauthenticated(actor_id, "meta", path)
        if not myself:
            return  # Response already set

        trustee_root = myself.store.trustee_root if myself.store else None
        if not trustee_root:
            trustee_root = ""
        if not path:
            values = {
                "id": actor_id,
                "type": self.config.aw_type,
                "version": self.config.version,
                "desc": self.config.desc,
                "info": self.config.info,
                "trustee_root": trustee_root,
                "specification": self.config.specification,
                "aw_version": self.config.aw_version,
                "aw_supported": self.config.aw_supported,
                "aw_formats": self.config.aw_formats,
            }
            
            # Add supported trust types if available
            try:
                from ..trust_type_registry import get_registry
                registry = get_registry(self.config)
                trust_types = registry.list_types()
                if trust_types:
                    # Convert trust types to a simple list of names for the meta endpoint
                    supported_trust_types = [trust_type.name for trust_type in trust_types]
                    values["aw_trust_types"] = supported_trust_types
            except Exception:
                # If trust type registry is not available, don't include trust types
                pass
            out = json.dumps(values)
            if self.response:
                self.response.write(out)
            self.response.headers["Content-Type"] = "application/json"
            return

        elif path == "id":
            out = actor_id
        elif path == "type":
            out = self.config.aw_type
        elif path == "version":
            out = self.config.version
        elif path == "desc":
            out = self.config.desc + (myself.id or "")
        elif path == "info":
            out = self.config.info
        elif path == "trustee_root":
            out = trustee_root
        elif path == "specification":
            out = self.config.specification
        elif path == "actingweb/version":
            out = self.config.aw_version
        elif path == "actingweb/supported":
            out = self.config.aw_supported
        elif path == "actingweb/formats":
            out = self.config.aw_formats
        elif path == "actingweb/trust_types":
            # Dedicated endpoint for supported trust types with more details
            try:
                from ..trust_type_registry import get_registry
                registry = get_registry(self.config)
                trust_types = registry.list_types()
                if trust_types:
                    # Return detailed trust type information
                    trust_type_details = []
                    for trust_type in trust_types:
                        trust_type_details.append({
                            "name": trust_type.name,
                            "display_name": trust_type.display_name,
                            "description": getattr(trust_type, 'description', ''),
                            "created_by": trust_type.created_by
                        })
                    out = json.dumps(trust_type_details)
                else:
                    out = json.dumps([])
            except Exception as e:
                logging.error(f"Error retrieving trust types: {e}")
                out = json.dumps([])
            
            if self.response:
                self.response.write(out)
                self.response.headers["Content-Type"] = "application/json"
            return
        else:
            if self.response:
                self.response.set_status(404)
            return
        if self.response:
            self.response.write(out)
