import json
import logging
from builtins import str

from actingweb import actor
from actingweb.handlers import base_handler


class RootFactoryHandler(base_handler.BaseHandler):

    def get(self):
        if self.request.get("_method") == "POST":
            self.post()
            return
        if self.config.ui:
            self.response.template_values = {}
        else:
            self.response.set_status(404)

    def post(self):
        try:
            body = self.request.body
            if isinstance(body, bytes):
                body = body.decode("utf-8", "ignore")
            elif body is None:
                body = "{}"
            params = json.loads(body)
            is_json = True
            if "creator" in params:
                creator = params["creator"]
            else:
                creator = ""
            if "trustee_root" in params:
                trustee_root = params["trustee_root"]
            else:
                trustee_root = ""
            if "passphrase" in params:
                passphrase = params["passphrase"]
            else:
                passphrase = ""
        except ValueError:
            is_json = False
            creator = self.request.get("creator")
            trustee_root = self.request.get("trustee_root")
            passphrase = self.request.get("passphrase")
            
        # Normalise creator when using email login flow
        if isinstance(creator, str):
            creator = creator.strip()
            if "@" in creator:
                creator = creator.lower()

        if not is_json and creator:
            existing_actor = actor.Actor(config=self.config)
            if existing_actor.get_from_creator(creator):
                actor_id = existing_actor.id or ""
                redirect_target = f"/{actor_id}/www"
                if self.response:
                    self.response.set_redirect(redirect_target)
                    self.response.headers["Location"] = f"{self.config.root}{actor_id}/www"
                    self.response.set_status(302, "Found")
                return

        # Create actor using enhanced method with hooks and trustee_root
        myself = actor.Actor(config=self.config)
        if not myself.create(
            url=self.request.url or "",
            creator=creator,
            passphrase=passphrase,
            trustee_root=trustee_root,
            hooks=self.hooks
        ):
            # Check if this is a unique creator constraint violation
            if self.config and self.config.unique_creator and creator:
                # Check if creator already exists
                in_db = self.config.DbActor.DbActor()
                exists = in_db.get_by_creator(creator=creator)
                if exists:
                    self.response.set_status(403, "Creator already exists")
                    logging.warning(
                        "Creator already exists, cannot create new Actor("
                        + str(self.request.url)
                        + " "
                        + str(creator)
                        + ")"
                    )
                    return

            # Generic creation failure
            self.response.set_status(400, "Not created")
            logging.warning(
                "Was not able to create new Actor("
                + str(self.request.url)
                + " "
                + str(creator)
                + ")"
            )
            return
        self.response.headers["Location"] = str(self.config.root + (myself.id or ""))
        if self.config.www_auth == "oauth" and not is_json:
            self.response.set_redirect(self.config.root + (myself.id or "") + "/www")
            return
        pair = {
            "id": myself.id,
            "creator": myself.creator,
            "passphrase": str(myself.passphrase),
        }
        if trustee_root and isinstance(trustee_root, str) and len(trustee_root) > 0:
            pair["trustee_root"] = trustee_root
        if self.config.ui and not is_json:
            self.response.template_values = pair
            return
        out = json.dumps(pair)
        self.response.write(out)
        self.response.headers["Content-Type"] = "application/json"
        self.response.set_status(201, "Created")
