import logging
import urllib.parse
from typing import Dict, List

from lightctl.client.base_client import BaseClient

logger = logging.getLogger(__name__)


class WorkspaceClient(BaseClient):
    def workspaces_url(self) -> str:
        return urllib.parse.urljoin(self.url_base, f"/api/v1//workspaces/")

    def create_workspace(self, name: str):
        url = self.workspaces_url()
        payload = {"name": name}
        return self.post(url, payload)

    # def delete_workspace(self, workspace_id: str) -> Dict:
    #     url = urllib.parse.urljoin(self.workspaces_url)
    #     return self.delete(url, workspace_id)

    def list_workspaces(self) -> List[Dict]:
        return self.get(self.workspaces_url())
