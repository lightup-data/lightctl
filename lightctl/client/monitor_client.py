import logging
import urllib.parse
from typing import Dict, List, Optional

from lightctl.client.base_client import BaseClient
from lightctl.config import API_VERSION

logger = logging.getLogger(__name__)


class MonitorClient(BaseClient):
    @property
    def monitors_url(self) -> str:
        return urllib.parse.urljoin(self.url_base, f"/api/{API_VERSION}/monitors/")

    def list_monitors(self) -> List[Dict]:
        res = self.get(self.monitors_url)
        return res.get("data", [])

    def get_monitor(self, id: str) -> Dict:
        url = urllib.parse.urljoin(self.monitors_url, id)
        monitor = self.get(url)
        return monitor

    def get_monitor_by_name(self, name) -> List[Dict]:
        url = urllib.parse.urljoin(self.monitors_url, f"?names={name}")
        # name is not unique
        return self.get(url)

    def create_monitor(self, data) -> Dict:
        return self.post(self.monitors_url, data)

    def update_monitor(self, id, data) -> Dict:
        url = urllib.parse.urljoin(self.monitors_url, id)
        return self.put(url, data)

    def delete_monitor(self, id):
        self.delete(self.monitors_url, id)

    def get_monitors_by_metric(self, metric_uuid) -> List[Dict]:
        url = urllib.parse.urljoin(self.monitors_url, f"?metric_uuids={metric_uuid}")
        return self.get(url)

    def last_processed_timestamp(self, id) -> Optional[float]:
        monitor = self.get_monitor(id)
        if monitor is None:
            return None
        return monitor["status"]["lastSampleTs"]
