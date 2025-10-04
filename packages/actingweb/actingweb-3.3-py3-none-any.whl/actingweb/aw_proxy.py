import json
import logging
import requests
import base64

from actingweb import trust

try:
    from urllib.parse import urlencode as urllib_urlencode
except ImportError:
    from urllib.parse import urlencode as urllib_urlencode


class AwProxy:
    """Proxy to other trust peers to execute RPC style calls

    Initialise with either trust_target to target a specific
    existing trust or use peer_target for simplicity to use
    the trust established with the peer.
    """

    def __init__(self, trust_target=None, peer_target=None, config=None):
        self.config = config
        self.last_response_code = 0
        self.last_response_message = 0
        self.last_location = None
        self.peer_passphrase = None
        if trust_target and trust_target.trust:
            self.trust = trust_target
            self.actorid = trust_target.id
        elif peer_target and peer_target["id"]:
            self.actorid = peer_target["id"]
            self.trust = None
            # Capture peer passphrase if available for Basic fallback (creator 'trustee')
            if "passphrase" in peer_target and peer_target["passphrase"]:
                self.peer_passphrase = peer_target["passphrase"]
            if peer_target["peerid"]:
                self.trust = trust.Trust(
                    actor_id=self.actorid,
                    peerid=peer_target["peerid"],
                    config=self.config,
                ).get()
                if not self.trust or len(self.trust) == 0:
                    self.trust = None

    def _bearer_headers(self):
        return {"Authorization": "Bearer " + self.trust["secret"]} if self.trust and self.trust.get("secret") else {}

    def _basic_headers(self):
        if not self.peer_passphrase:
            return {}
        u_p = ("trustee:" + self.peer_passphrase).encode("utf-8")
        return {"Authorization": "Basic " + base64.b64encode(u_p).decode("utf-8")}

    def _maybe_retry_with_basic(self, method, url, data=None, headers=None):
        # Only retry if we have a peer passphrase available
        if not self.peer_passphrase:
            return None
        try:
            bh = self._basic_headers()
            if data is None:
                if method == "GET":
                    return requests.get(url=url, headers=bh, timeout=(5, 10))
                if method == "DELETE":
                    return requests.delete(url=url, headers=bh, timeout=(5, 10))
            else:
                if method == "POST":
                    return requests.post(url=url, data=data, headers={**bh, "Content-Type": "application/json"}, timeout=(5, 10))
                if method == "PUT":
                    return requests.put(url=url, data=data, headers={**bh, "Content-Type": "application/json"}, timeout=(5, 10))
        except Exception:
            return None
        return None

    def get_resource(self, path=None, params=None):
        if not path or len(path) == 0:
            return None
        if not params:
            params = {}
        if not self.trust or not self.trust["baseuri"] or not self.trust["secret"]:
            return None
        url = self.trust["baseuri"].strip("/") + "/" + path.strip("/")
        if params:
            url = url + "?" + urllib_urlencode(params)
        headers = self._bearer_headers()
        logging.debug("Getting trust peer resource at (" + url + ")")
        try:
            response = requests.get(url=url, headers=headers, timeout=(5, 10))
            # Retry with Basic if Bearer gets redirected/unauthorized/forbidden
            if response.status_code in (302, 401, 403):
                retry = self._maybe_retry_with_basic("GET", url)
                if retry is not None:
                    response = retry
            self.last_response_code = response.status_code
            self.last_response_message = response.content
        except Exception:
            logging.debug("Not able to get peer resource")
            self.last_response_code = 408
            return {
                "error": {
                    "code": 408,
                    "message": "Unable to communciate with trust peer service.",
                },
            }
        logging.debug(
            "Get trust peer resource POST response:("
            + str(response.status_code)
            + ") "
            + str(response.content)
        )
        if response.status_code < 200 or response.status_code > 299:
            logging.info("Not able to get trust peer resource.")
        try:
            result = response.json()
        except (TypeError, ValueError, KeyError):
            logging.debug(
                "Not able to parse response when getting resource at(" + url + ")"
            )
            result = {}
        return result

    def create_resource(self, path=None, params=None):
        if not path or len(path) == 0:
            return None
        if not params:
            params = {}
        if not self.trust or not self.trust["baseuri"] or not self.trust["secret"]:
            return None
        data = json.dumps(params)
        headers = {**self._bearer_headers(), "Content-Type": "application/json"}
        url = self.trust["baseuri"].strip("/") + "/" + path.strip("/")
        logging.debug(
            "Creating trust peer resource at (" + url + ") with data(" + str(data) + ")"
        )
        try:
            response = requests.post(
                url=url, data=data, headers=headers, timeout=(5, 10)
            )
            if response.status_code in (302, 401, 403):
                retry = self._maybe_retry_with_basic("POST", url, data=data)
                if retry is not None:
                    response = retry
            self.last_response_code = response.status_code
            self.last_response_message = response.content
        except Exception:
            logging.debug("Not able to create new peer resource")
            self.last_response_code = 408
            return {
                "error": {
                    "code": 408,
                    "message": "Unable to communciate with trust peer service.",
                },
            }
        if "Location" in response.headers:
            self.last_location = response.headers["Location"]
        else:
            self.last_location = None
        logging.debug(
            "Create trust peer resource POST response:("
            + str(response.status_code)
            + ") "
            + str(response.content)
        )
        if response.status_code < 200 or response.status_code > 299:
            logging.warning("Not able to create new trust peer resource.")
        try:
            result = response.json()
        except (TypeError, ValueError, KeyError):
            logging.debug(
                "Not able to parse response when creating resource at(" + url + ")"
            )
            result = {}
        return result

    def change_resource(self, path=None, params=None):
        if not path or len(path) == 0:
            return None
        if not params:
            params = {}
        if not self.trust or not self.trust["baseuri"] or not self.trust["secret"]:
            return None
        data = json.dumps(params)
        headers = {"Authorization": "Bearer " + self.trust["secret"], "Content-Type": "application/json"}
        url = self.trust["baseuri"].strip("/") + "/" + path.strip("/")
        logging.debug(
            "Changing trust peer resource at (" + url + ") with data(" + str(data) + ")"
        )
        try:
            response = requests.put(
                url=url, data=data, headers=headers, timeout=(5, 10)
            )
            if response.status_code in (302, 401, 403):
                retry = self._maybe_retry_with_basic("PUT", url, data=data)
                if retry is not None:
                    response = retry
            self.last_response_code = response.status_code
            self.last_response_message = response.content
        except Exception:
            logging.debug("Not able to change peer resource")
            self.last_response_code = 408
            return {
                "error": {
                    "code": 408,
                    "message": "Unable to communciate with trust peer service.",
                },
            }
        logging.debug(
            "Change trust peer resource PUT response:("
            + str(response.status_code)
            + ") "
            + str(response.content)
        )
        if response.status_code < 200 or response.status_code > 299:
            logging.warning("Not able to change trust peer resource.")
        try:
            result = response.json()
        except (TypeError, ValueError, KeyError):
            logging.debug(
                "Not able to parse response when changing resource at(" + url + ")"
            )
            result = {}
        return result

    def delete_resource(self, path=None):
        if not path or len(path) == 0:
            return None
        if not self.trust or not self.trust["baseuri"] or not self.trust["secret"]:
            return None
        headers = {"Authorization": "Bearer " + self.trust["secret"]}
        url = self.trust["baseuri"].strip("/") + "/" + path.strip("/")
        logging.debug("Deleting trust peer resource at (" + url + ")")
        try:
            response = requests.delete(
                url=url, headers=headers, timeout=(5, 10)
            )
            if response.status_code in (302, 401, 403):
                retry = self._maybe_retry_with_basic("DELETE", url)
                if retry is not None:
                    response = retry
            self.last_response_code = response.status_code
            self.last_response_message = response.content
        except Exception:
            logging.debug("Not able to delete peer resource")
            self.last_response_code = 408
            return {
                "error": {
                    "code": 408,
                    "message": "Unable to communciate with trust peer service.",
                },
            }
