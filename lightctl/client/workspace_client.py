import logging
import urllib.parse
from typing import Dict, List

from lightctl.client.base_client import BaseClient

logger = logging.getLogger(__name__)


class WorkspaceClient(BaseClient):
    def workspaces_url(self) -> str:
        return urllib.parse.urljoin(self.url_base, f"/api/v1/workspaces/")

    def deactivate_workspace_url(self, workspace_id) -> str:
        return urllib.parse.urljoin(self.url_base, f"/api/v1/ws/{workspace_id}/workspaces/deactivate")

    def create_workspace(self, name: str):
        url = self.workspaces_url()
        payload = {"name": name}
        res = self.post(url, payload)
        return res["data"]

    def deactivate_workspace(self, workspace_id: str):
        url = self.deactivate_workspace_url(workspace_id)
        return self.post(url, {}, expected_status=204)

    # def delete_workspace(self, workspace_id: str) -> Dict:
    #     url = urllib.parse.urljoin(self.workspaces_url)
    #     return self.delete(url, workspace_id)

    def list_workspaces(self) -> List[Dict]:
        res = self.get(self.workspaces_url())
        return res["data"]
