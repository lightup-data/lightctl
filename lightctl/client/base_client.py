import datetime
import functools
import json
import logging
import os.path
import urllib.parse
from typing import Dict

import requests

from lightctl.config import PASSWORD, URL_BASE, USERNAME
from lightctl.util import check_status_code

logger = logging.getLogger(__name__)


def _logged_in(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        self.login_if_needed()
        return func(self, *args, **kwargs)

    return wrapper


class BaseClient:
    CSRF_TOKEN_KEY = "csrftoken"

    def __init__(self):
        self.client = requests.session()
        self.url_base = URL_BASE
        self._logged_in = False

    @property
    def log_url(self):
        return urllib.parse.urljoin(self.url_base, "api/v0/users/login-basic-auth/")

    def login_if_needed(self):
        for cookie in self.client.cookies:
            if cookie.is_expired():
                self._logged_in = False

        if self._logged_in:
            return

        # TODO: CSRF token for login
        login_data = {
            "auth_info": {"type": "basic", "username": USERNAME, "password": PASSWORD}
        }
        res = self.client.post(
            self.log_url, json=login_data, headers=dict(Referer=self.log_url)
        )
        if res.status_code == 200:
            self._logged_in = True
            return

        logger.warning(f"login failed {res.text}")
        self._logged_in = False

    @_logged_in
    def get(self, endpoint) -> Dict:
        r = self.client.get(endpoint)
        check_status_code(r, 200)
        return json.loads(r.text)

    @_logged_in
    def post(self, endpoint, data: Dict):
        headers = self._prepare_post_put_headers()
        data = json.dumps(data, default=_json_serial)
        r = self.client.post(endpoint, data=data, headers=headers)
        check_status_code(r, 201)
        return json.loads(r.text)

    @_logged_in
    def delete(self, endpoint, id):
        assert self.CSRF_TOKEN_KEY in self.client.cookies
        csrf_token = self.client.cookies[self.CSRF_TOKEN_KEY]
        r = self.client.delete(
            os.path.join(endpoint, str(id)), headers={"X-CSRFTOKEN": csrf_token}
        )
        check_status_code(r, 204)
        return {"id": id}

    @_logged_in
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


def _json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, (datetime.datetime, datetime.date)):
        return obj.isoformat() + "Z"
    raise TypeError("Type %s not serializable" % type(obj))
