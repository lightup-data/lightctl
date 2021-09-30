import logging
import urllib.parse
from typing import Dict, List

from lightctl.client.base_client import BaseClient
from lightctl.config import API_VERSION

logger = logging.getLogger(__name__)


class MetricClient(BaseClient):
    @property
    def metrics_url(self) -> str:
        return urllib.parse.urljoin(self.url_base, f"/api/{API_VERSION}/metrics/")

    def list_metrics(self) -> List[Dict]:
        return self.get(self.metrics_url)

    def get_metric(self, id: str) -> Dict:
        url = urllib.parse.urljoin(self.metrics_url, id)
        return self.get(url)

    def get_metric_by_name(self, name: str) -> Dict:
        url = urllib.parse.urljoin(self.metrics_url, f"?name={name}")
        return self.get(url)

    def create_metric(self, data: Dict) -> Dict:
        return self.post(self.metrics_url, data)

    def update_metric(self, id: str, data: Dict, force: bool = False) -> Dict:
        url = urllib.parse.urljoin(self.metrics_url, id)
        return self.put(url, data, force=force)

    def delete_metric(self, id: str, force: bool = False):
        self.delete(self.metrics_url, id, force=force)

    def inspect_schema(self, data: Dict) -> Dict:
        url = urllib.parse.urljoin(self.metrics_url, "schema")
        return self.post(url, data, expected_status=200)

    def inspect_data(self, data: Dict) -> Dict:
        url = urllib.parse.urljoin(self.metrics_url, "preview")
        return self.post(url, data, expected_status=200)

    def inspect_distinct_values(self, data: Dict) -> List:
        url = urllib.parse.urljoin(self.metrics_url, "distinct-values")
        return self.post(url, data, expected_status=200)

    def get_schema(self, id: str) -> List:
        url = urllib.parse.urljoin(self.metrics_url, f"{id}/schema")
        return self.get(url)
