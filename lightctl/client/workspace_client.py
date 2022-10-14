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

    def list_workspace_schedules(self, workspace_id: str) -> List[Dict]:
        """Returns a list of schedules for a Workspace."""
        return self.get(urllib.parse.urljoin(self.url_base, f"/api/v0/ws/{workspace_id}/schedules/"))

    def list_workspace_users(self, workspace_id: str) -> List[Dict]:
        """Returns a list of users for a Workspace."""
        return self.get(urllib.parse.urljoin(self.url_base, f"/api/v0/ws/{workspace_id}/users/"))

    def get_workspace_tags(self, workspace_id: str) -> List:
        """Returns a list of unique tags in a Workspace."""
        return self.get(urllib.parse.urljoin(self.url_base, f"/api/v0/ws/{workspace_id}/tags/"))

    def list_workspace_channels(self, workspace_id: str) -> List[Dict]:
        """Returns a list of alert notification channels in a Workspace."""
        return self.get(urllib.parse.urljoin(self.url_base, f"/api/v0/ws/{workspace_id}/alerting-channels/"))

    def list_workspace_events(self, workspace_id: str, start_ts: int = None, end_ts: int = None) -> List[Dict]:
        """Returns a list of alert notification channels in a Workspace."""
        start_ts = f"?start_ts={start_ts}" if start_ts else ""
        end_ts = f"&end_ts={end_ts}" if end_ts else ""
        url = (
                self.url_base
                + f"/api/v0/ws/{workspace_id}/events/"
                + f"{start_ts}{end_ts}"
        )
        return self.get(url).get("data")
