import logging
import urllib.parse

from lightctl.client.base_client import BaseClient
from lightctl.config import API_VERSION

logger = logging.getLogger(__name__)


class MetricClient(BaseClient):
    @property
    def metrics_url(self):
        return urllib.parse.urljoin(self.url_base, f"/api/{API_VERSION}/metrics/")

    def list_metrics(self):
        return self.get(self.metrics_url)

    def get_metric(self, id: str):
        url = urllib.parse.urljoin(self.metrics_url, id)
        return self.get(url)

    # TODO: [v1] support query in backend
    def get_metric_by_name(self, name):
        metrics = self.list_metrics()
        for metric in metrics:
            if metric["metadata"]["name"] == name:
                return metric
        return None

    def create_metric(self, data):
        return self.post(self.metrics_url, data)

    def update_metric(self, id, data, force=False):
        url = urllib.parse.urljoin(self.metrics_url, id)
        return self.put(url, data, force=force)

    def delete_metric(self, id, force=False):
        self.delete(self.metrics_url, id, force=force)

    # TODO: [prod] better naming for "inspect-*" sub command
    def inspect_schema(self, data):
        url = urllib.parse.urljoin(self.metrics_url, "schema")
        return self.post(url, data, expected_status=200)

    def inspect_data(self, data):
        url = urllib.parse.urljoin(self.metrics_url, "preview")
        return self.post(url, data, expected_status=200)

    def inspect_distinct_values(self, data):
        url = urllib.parse.urljoin(self.metrics_url, "distinct-values")
        return self.post(url, data, expected_status=200)

    def get_schema(self, id):
        url = urllib.parse.urljoin(self.metrics_url, f"{id}/schema")
        return self.get(url)
