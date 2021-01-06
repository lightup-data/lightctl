import datetime
import functools
import json
import logging
import os.path
import urllib
from pathlib import Path
from typing import Dict, Optional

import requests

from lightctl.config import URL_BASE
from lightctl.util import check_status_code

logger = logging.getLogger(__name__)
true = True
credential = {
    "user": {"username": "Yiqian Zhou", "email": "yiqian@lightup.ai"},
    "jti": "c1b111121e154eddbfe6221d51533384",
    "created": "2021-01-06 23:50:23.120167+00:00",
    "expired": "2021-01-07 23:50:23+00:00",
    "active": true,
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA5OTc3MzIzLCJqdGkiOiI2NTJlNjVjNDk3ODE0MjcyODM0ZTQwYzEwNDUyMTBkZSIsInVzZXJfaWQiOjN9.dEZ9ix0KgoB6lxg9ltkbPKBgjNAgCiQBw6pBj4bvWM0",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxMDA2MzQyMywianRpIjoiYzFiMTExMTIxZTE1NGVkZGJmZTYyMjFkNTE1MzMzODQiLCJ1c2VyX2lkIjozfQ.DkaQstsOeOXh5p38LIgLjWeZ3fBzcnHZtlNv7T78C8Y",
}

c2 = {
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxMDA2MzU1NiwianRpIjoiYWU2OGM2M2FmNmQ1NDlkNTgwOTg5YWM2MGJlYjY0NjEiLCJ1c2VyX2lkIjoxfQ.RpsWmwhwj-jN6KYzzAxdECzc1IG5L8tJ3dOm1DbmPD8",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA5OTc3NDU2LCJqdGkiOiJiNjNjZGFlNjhlYzA0NjU1Yjg4ZmRiOTdlYWVhOGE2YiIsInVzZXJfaWQiOjF9.y2GOiVY_U0jMz1nDrqOff561tR2IiU_Fb2ufyV4Jf90",
}


def refresh_token_if_needed(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        res = func(self, *args, **kwargs)
        if res.status_code == 401 and res.json().get("code") == "token_not_valid":
            self._refresh_access_token()
            res = func(self, *args, **kwargs)
        return res

    return wrapper


class BaseClient:
    CSRF_TOKEN_KEY = "csrftoken"
    credential_file_path = os.path.join(str(Path.home()), ".lightup", "cli-credential")
    cached_access_token_file_path = os.path.join(
        str(Path.home()), ".lightup", "cached-cli-access-token"
    )

    def __init__(self):
        with open(self.credential_file_path) as f:
            self.credential = json.load(f)
            self.refresh_token = self.credential["refresh"]

        # self.access_token: Optional[str] = self._get_cached_access_token()
        self.access_token = c2["access"]

        if not self.access_token:
            self._refresh_access_token()

        self.url_base = URL_BASE

        self.client = requests.session()

    @refresh_token_if_needed
    def _get(self, *args, **kwargs):
        # kwargs["headers"].update({"Authorization": f"Bearer {self.access_token}"})
        kwargs["headers"] = {"Authorization": f"Bearer {self.access_token}"}
        return requests.get(*args, **kwargs)

    def get(self, endpoint) -> Dict:
        headers = {"Authorization": f"Bearer {self.access_token}"}
        r = self._get(endpoint, headers=headers)
        check_status_code(r, 200)
        return json.loads(r.text)

    def post(self, endpoint, data: Dict, expected_status=201):
        headers = self._prepare_post_put_headers()
        data = json.dumps(data, default=_json_serial)
        r = self.client.post(endpoint, data=data, headers=headers)
        check_status_code(r, expected_status)
        return json.loads(r.text)

    def delete(self, endpoint, id):
        assert self.CSRF_TOKEN_KEY in self.client.cookies
        csrf_token = self.client.cookies[self.CSRF_TOKEN_KEY]
        r = self.client.delete(
            os.path.join(endpoint, str(id)), headers={"X-CSRFTOKEN": csrf_token}
        )
        check_status_code(r, 204)
        return {"id": id}

    def put(self, endpoint, id, data: Dict):
        headers = self._prepare_post_put_headers()
        data = json.dumps(data, default=_json_serial)
        r = self.client.put(os.path.join(endpoint, str(id)), data=data, headers=headers)
        check_status_code(r, 200)
        return json.loads(r.text)

    def _prepare_post_put_headers(self):
        assert self.CSRF_TOKEN_KEY in self.client.cookies
        csrf_token = self.client.cookies[self.CSRF_TOKEN_KEY]
        headers = {
            "X-CSRFTOKEN": csrf_token,
            "Content-type": "application/json",
            "Accept": "text/plain, application/json",
        }
        return headers

    def _get_cached_access_token(self) -> Optional[str]:
        if not Path(self.cached_access_token_file_path).exists():
            return None
        with open(self.cached_access_token_file_path, "r") as f:
            return f.read()

    def _set_cached_access_token(self, token: str):
        with open(self.cached_access_token_file_path, "w") as f:
            return f.write(token)

    def _refresh_access_token(self):
        endpoint = urllib.parse.urljoin(self.url_base, "/api/token/refresh/")
        data = {"refresh": self.refresh_token}
        res = requests.post(endpoint, json=data)
        self.access_token = res.json()["access"]
        self._set_cached_access_token(self.access_token)


def _json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, (datetime.datetime, datetime.date)):
        return obj.isoformat() + "Z"
    raise TypeError("Type %s not serializable" % type(obj))
