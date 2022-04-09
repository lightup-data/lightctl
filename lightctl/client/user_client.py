import logging
import urllib.parse
from typing import Dict, List

from lightctl.client.base_client import BaseClient

logger = logging.getLogger(__name__)


class UserClient(BaseClient):
    def users_url(self, workspace_id) -> str:
        return urllib.parse.urljoin(self.url_base, f"/api/v0/ws/{workspace_id}/users/")

    def add_user_to_workspace(self, workspace_id: str, user_id: str, role: str) -> Dict:
        url = self.users_url(workspace_id)
        payload = {"email": user_id, "role": role}
        res = self.post(url, payload)
        return res

    def remove_user_from_workspace(self, workspace_id: str, user_id: str) -> Dict:
        url = self.users_url(workspace_id)
        return self.delete(url, user_id)

    def update_user_role(self, workspace_id: str, user_id: str, role: str):
        url = urllib.parse.urljoin(self.users_url(workspace_id), user_id)
        payload = {"role": role}
        self.patch(url, payload)

    def list_users(self, workspace_id: str) -> List[Dict]:
        res = self.get(self.users_url(workspace_id))
        return res
