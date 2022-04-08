import logging
import urllib.parse
from typing import Dict, List

from lightctl.client.base_client import BaseClient

logger = logging.getLogger(__name__)


class WorkspaceClient(BaseClient):
    def workspaces_url(self, workspace_id) -> str:
        return urllib.parse.urljoin(self.url_base, f"/api/v1//workspaces/")

    def create_workspace(self, workspace_id: str, name: str):
        url = self.workspaces_url(workspace_id)
        payload = {"name": name, "uuid": workspace_id}
        return self.post(url, payload)

    def delete_workspace(self, workspace_id: str, force=False) -> Dict:
        url = urllib.parse.urljoin(self.workspaces_url(workspace_id))
        return self.delete(url, workspace_id, force)

    def list_workspaces(self, workspace_id: str) -> List[Dict]:
        return self.get(self.workspaces_url(workspace_id))
