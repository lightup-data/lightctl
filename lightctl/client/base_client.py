import datetime
import functools
import json
import logging
import os.path
import urllib.parse
from pathlib import Path
from typing import Dict, Optional

import requests

from lightctl.config import ACCESS_TOKEN_CACHE_FILE_PATH, CREDENTIAL_FILE_PATH
from lightctl.util import check_status_code

logger = logging.getLogger(__name__)


def refresh_token_if_needed(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if not self.access_token:
            self._refresh_access_token()

        res = func(self, *args, **kwargs)
        if res.status_code == 401 and res.json().get("code") == "token_not_valid":
            self._refresh_access_token()
            res = func(self, *args, **kwargs)
        return res

    return wrapper


class BaseClient:
    def __init__(self):
        with open(CREDENTIAL_FILE_PATH) as f:
            self.credential = json.load(f)
            self.refresh_token = self.credential["refresh"]
            self.url_base = self.credential["server"]

        self.access_token: Optional[str] = self._get_cached_access_token()

    def get(self, endpoint) -> Dict:
        r = self._get(endpoint)
        check_status_code(r, 200)
        return json.loads(r.text)

    def post(self, endpoint, data: Dict, expected_status=201):
        data = json.dumps(data, default=_json_serial)
        r = self._post(endpoint, data=data)
        check_status_code(r, expected_status)
        return json.loads(r.text)

    def delete(self, endpoint, id):
        r = self._delete(os.path.join(endpoint, str(id)))
        check_status_code(r, 204)
        return {"id": id}

    def put(self, endpoint, id, data: Dict):
        data = json.dumps(data, default=_json_serial)
        r = self._put(os.path.join(endpoint, str(id)), data=data)
        check_status_code(r, 200)
        return json.loads(r.text)

    @refresh_token_if_needed
    def _get(self, *args, **kwargs):
        headers = kwargs.get("headers", {})
        headers["Authorization"] = f"Bearer {self.access_token}"
        return requests.get(*args, **kwargs, headers=headers)

    @refresh_token_if_needed
    def _post(self, *args, **kwargs):
        headers = kwargs.get("headers", {})
        headers["Authorization"] = f"Bearer {self.access_token}"
        return requests.post(*args, **kwargs, headers=headers)

    @refresh_token_if_needed
    def _delete(self, *args, **kwargs):
        headers = kwargs.get("headers", {})
        headers["Authorization"] = f"Bearer {self.access_token}"
        return requests.delete(*args, **kwargs, headers=headers)

    @refresh_token_if_needed
    def _put(self, *args, **kwargs):
        headers = kwargs.get("headers", {})
        headers["Authorization"] = f"Bearer {self.access_token}"
        return requests.put(*args, **kwargs, headers=headers)

    def _refresh_access_token(self):
        endpoint = urllib.parse.urljoin(self.url_base, "/api/token/refresh/")
        data = {"refresh": self.refresh_token}
        res = requests.post(endpoint, json=data)
        check_status_code(res, 200)
        self.access_token = res.json()["access"]
        logger.debug("access token refreshed")
        self._set_cached_access_token(self.access_token)
        logger.debug("access token cached")

    @staticmethod
    def _get_cached_access_token() -> Optional[str]:
        if not Path(ACCESS_TOKEN_CACHE_FILE_PATH).exists():
            return None
        with open(ACCESS_TOKEN_CACHE_FILE_PATH, "r") as f:
            return f.read()

    @staticmethod
    def _set_cached_access_token(token: str):
        with open(ACCESS_TOKEN_CACHE_FILE_PATH, "w") as f:
            return f.write(token)


def _json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, (datetime.datetime, datetime.date)):
        return obj.isoformat() + "Z"
    raise TypeError("Type %s not serializable" % type(obj))
