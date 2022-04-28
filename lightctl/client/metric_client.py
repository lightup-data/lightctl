import logging
import urllib.parse
from typing import Dict, List
from uuid import UUID

from lightctl.client.base_client import BaseClient
from lightctl.config import API_VERSION

logger = logging.getLogger(__name__)


class MetricClient(BaseClient):
    def metrics_url(self, workspace_id: str) -> str:
        return urllib.parse.urljoin(
            self.url_base, f"/api/{API_VERSION}/ws/{workspace_id}/metrics/"
        )

    def list_metrics(self, workspace_id: str) -> List[Dict]:
        return self.get(self.metrics_url(workspace_id))

    def get_metric(self, workspace_id: str, id: UUID) -> Dict:
        url = urllib.parse.urljoin(self.metrics_url(workspace_id), f"{id}")
        return self.get(url)

    def get_metric_by_name(self, workspace_id: str, name: str) -> List[Dict]:
        url = urllib.parse.urljoin(self.metrics_url(workspace_id), f"?name={name}")
        return self.get(url)

    def create_metric(self, workspace_id: str, data: Dict) -> Dict:
        return self.post(self.metrics_url(workspace_id), data)

    def update_metric(
        self, workspace_id: str, id: UUID, data: Dict, force: bool = False
    ) -> Dict:
        url = urllib.parse.urljoin(self.metrics_url(workspace_id), f"{id}")
        return self.put(url, data, force=force)

    def delete_metric(self, workspace_id: str, id: UUID, force: bool = False):
        self.delete(self.metrics_url(workspace_id), f"{id}", force=force)
