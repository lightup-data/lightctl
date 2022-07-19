import logging
import urllib.parse
from typing import Dict, List

from lightctl.client.base_client import BaseClient

logger = logging.getLogger(__name__)


class WorkspaceClient(BaseClient):
    def workspaces_url(self) -> str:
        return urllib.parse.urljoin(self.url_base, f"/api/v1/workspaces/")

    def create_workspace(self, name: str):
        url = self.workspaces_url()
        payload = {"name": name}
        res = self.post(url, payload)
        return res["data"]

    def delete_workspace(self, workspace_id: str) -> Dict:
        # note that delete workspace is associated with different url.
        url = urllib.parse.urljoin(self.url_base, "/api/v1/ws/")
        return self.delete(url, workspace_id, force=True)

    def list_workspaces(self) -> List[Dict]:
        res = self.get(self.workspaces_url())
        return res["data"]
