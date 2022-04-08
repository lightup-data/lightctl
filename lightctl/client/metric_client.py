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

    def get_metric(self, workspace_id: str, id: str) -> Dict:
        assert UUID(id)
        url = urllib.parse.urljoin(self.metrics_url(workspace_id), id)
        return self.get(url)

    def get_metric_by_name(self, workspace_id: str, name: str) -> Dict:
        url = urllib.parse.urljoin(self.metrics_url(workspace_id), f"?name={name}")
        return self.get(url)

    def create_metric(self, workspace_id: str, data: Dict) -> Dict:
        return self.post(self.metrics_url(workspace_id), data)

    def update_metric(
        self, workspace_id: str, id: str, data: Dict, force: bool = False
    ) -> Dict:
        url = urllib.parse.urljoin(self.metrics_url(workspace_id), id)
        return self.put(url, data, force=force)

    def delete_metric(self, workspace_id: str, id: str, force: bool = False):
        assert UUID(id)
        self.delete(self.metrics_url(workspace_id), id, force=force)

    def inspect_schema(self, workspace_id: str, data: Dict) -> Dict:
        url = urllib.parse.urljoin(self.metrics_url(workspace_id), "schema")
        return self.post(url, data, expected_status=200)

    def inspect_data(self, workspace_id: str, data: Dict) -> Dict:
        url = urllib.parse.urljoin(self.metrics_url(workspace_id), "preview")
        return self.post(url, data, expected_status=200)

    def inspect_distinct_values(self, workspace_id: str, data: Dict) -> List:
        url = urllib.parse.urljoin(self.metrics_url(workspace_id), "distinct-values")
        return self.post(url, data, expected_status=200)

    def get_schema(self, workspace_id: str, id: str) -> List:
        assert UUID(id)
        url = urllib.parse.urljoin(self.metrics_url(workspace_id), f"{id}/schema")
        return self.get(url)
