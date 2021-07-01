import logging
import urllib.parse

from lightctl.client.base_client import BaseClient
from lightctl.config import API_VERSION

logger = logging.getLogger(__name__)


class SourceClient(BaseClient):
    @property
    def sources_url(self):
        return urllib.parse.urljoin(self.url_base, f"/api/{API_VERSION}/sources/")

    def list_sources(self):
        return self.get(self.sources_url)

    def get_source(self, id: str):
        url = urllib.parse.urljoin(self.sources_url, id)
        return self.get(url)

    def get_source_by_name(self, name):
        sources = self.list_sources()
        for source in sources:
            if source["name"] == name:
                return source
        return None

    def create_source(self, data):
        return self.post(self.sources_url, data)

    def update_source(self, id, data):
        url = urllib.parse.urljoin(self.sources_url, id)
        return self.put(url, data)

    def delete_source(self, id):
        self.delete(self.sources_url, id)

    def inspect(self, data):
        url = urllib.parse.urljoin(
            self.url_base, f"/api/{API_VERSION}/sources-inspection"
        )
        return self.post(url, data, expected_status=200)

    def list_tables(self, id):
        url = urllib.parse.urljoin(
            self.url_base, f"/api/{API_VERSION}/sources/{id}/profile/tables"
        )
        tables = self.get(url)
        return tables

    def get_schema(self, id, table_name):
        url = urllib.parse.urljoin(
            self.url_base,
            f"/api/{API_VERSION}sources/{id}/schema?table_name={table_name}",
        )
        return self.get(url)

    def update_profiler_config(self, id, table_uuid, data):
        url = urllib.parse.urljoin(
            self.url_base,
            f"/api/{API_VERSION}/sources/{id}/profile/tables/{table_uuid}/profiler-config",
        )
        return self.put(url, data)
