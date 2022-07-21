import logging
import urllib.parse
from typing import Dict, List

from lightctl.client.base_client import BaseClient

logger = logging.getLogger(__name__)


class UserClient(BaseClient):
    def app_users_url(self) -> str:
        return urllib.parse.urljoin(self.url_base, "/api/v0/users/")

    def add_app_user(self, user_id: str, role: str) -> Dict:
        assert role in ["app_admin", "app_editor", "app_viewer"]
        url = self.app_users_url()
        payload = {"email": user_id, "app_role": role}
        res = self.post(url, payload)
        return res

    def update_app_user_role(self, user_id: str, role: str):
        assert role in ["app_admin", "app_editor", "app_viewer"]
        quoted_user = urllib.parse.quote_plus(user_id)
        url = urllib.parse.urljoin(self.app_users_url(), quoted_user)
        payload = {"role": role}
        return self.patch(url, payload)

    def delete_app_user(self, user_id: str):
        quoted_user = urllib.parse.quote_plus(user_id)
        url = self.app_users_url()
        res = self.delete(url, quoted_user, force=True)
        return res

    def get_app_user(self, user_id: str):
        quoted_user = urllib.parse.quote_plus(user_id)
        url = urllib.parse.urljoin(self.app_users_url(), quoted_user)
        return self.get(url)

    def list_app_users(self) -> List[Dict]:
        res = self.get(self.app_users_url())
        return res

    def users_url(self, workspace_id) -> str:
        return urllib.parse.urljoin(self.url_base, f"/api/v0/ws/{workspace_id}/users/")

    def add_user_to_workspace(self, workspace_id: str, user_id: str, role: str) -> Dict:
        url = self.users_url(workspace_id)
        payload = {"email": user_id, "role": role}
        res = self.post(url, payload)
        return res

    def remove_user_from_workspace(self, workspace_id: str, user_id: str) -> Dict:
        url = self.users_url(workspace_id)
        quoted_user = urllib.parse.quote_plus(user_id)
        return self.delete(url, quoted_user, force=True)

    def update_user_role(self, workspace_id: str, user_id: str, role: str):
        quoted_user = urllib.parse.quote_plus(user_id)
        url = urllib.parse.urljoin(self.users_url(workspace_id), quoted_user)
        payload = {"role": role}
        return self.patch(url, payload)

    def list_users(self, workspace_id: str) -> List[Dict]:
        res = self.get(self.users_url(workspace_id))
        return res
