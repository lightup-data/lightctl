import logging
import urllib.parse
from typing import Dict, List, Optional
from uuid import UUID

from lightctl.client.base_client import BaseClient
from lightctl.config import API_VERSION

logger = logging.getLogger(__name__)


class MonitorClient(BaseClient):
    def monitors_url(self, workspace_id: str) -> str:
        return urllib.parse.urljoin(
            self.url_base, f"/api/{API_VERSION}/ws/{workspace_id}/monitors/"
        )

    def list_monitors(self, workspace_id: str) -> List[Dict]:
        res = self.get(self.monitors_url(workspace_id))
        return res.get("data", [])

    def get_monitor(self, workspace_id: str, id: UUID) -> Dict:
        url = urllib.parse.urljoin(self.monitors_url(workspace_id), f"{id}")
        monitor = self.get(url)
        return monitor

    def get_monitor_by_name(self, workspace_id: str, name: str) -> List[Dict]:
        url = urllib.parse.urljoin(self.monitors_url(workspace_id), f"?names={name}")
        # name is not unique
        return self.get(url)

    def create_monitor(self, workspace_id: str, data: Dict) -> Dict:
        return self.post(self.monitors_url(workspace_id), data)

    def update_monitor(self, workspace_id: str, id: UUID, data: Dict) -> Dict:
        url = urllib.parse.urljoin(self.monitors_url(workspace_id), f"{id}")
        return self.put(url, data)

    def delete_monitor(self, workspace_id: str, id: UUID):
        self.delete(self.monitors_url(workspace_id), f"{id}")

    def get_monitors_by_metric(
        self, workspace_id: str, metric_uuid: UUID
    ) -> List[Dict]:
        url = urllib.parse.urljoin(
            self.monitors_url(workspace_id), f"?metric_uuids={metric_uuid}"
        )
        return self.get(url)

    def last_processed_timestamp(self, workspace_id: str, id: UUID) -> Optional[float]:
        monitor = self.get_monitor(id, workspace_id)
        if monitor is None:
            return None
        return monitor["status"]["lastSampleTs"]
