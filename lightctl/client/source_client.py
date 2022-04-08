import logging
import urllib.parse
from typing import Dict, List, Optional

from lightctl.client.base_client import BaseClient
from lightctl.config import API_VERSION

logger = logging.getLogger(__name__)


class SourceClient(BaseClient):
    @property
    def sources_url(self) -> str:
        return urllib.parse.urljoin(self.url_base, f"/api/{API_VERSION}/sources/")

    def list_sources(self) -> List[Dict]:
        return self.get(self.sources_url)

    def get_source(self, id: str) -> Dict:
        url = urllib.parse.urljoin(self.sources_url, id)
        return self.get(url)

    def get_source_by_name(self, name: str) -> Optional[Dict]:
        sources = self.list_sources()
        for source in sources:
            if source["name"] == name:
                return source
        return None

    def create_source(self, data: Dict) -> Dict:
        return self.post(self.sources_url, data)

    def update_source(self, id, data: Dict) -> Dict:
        url = urllib.parse.urljoin(self.sources_url, id)
        return self.put(url, data)

    def delete_source(self, id: str) -> Dict:
        self.delete(self.sources_url, id)

    def inspect(self, data: Dict) -> Dict:
        url = urllib.parse.urljoin(
            self.url_base, f"/api/{API_VERSION}/sources/inspection"
        )
        return self.post(url, data, expected_status=200)

    def list_tables(self, id: str) -> List[Dict]:
        url = urllib.parse.urljoin(
            self.url_base, f"/api/{API_VERSION}/sources/{id}/profile/tables"
        )
        tables = self.get(url)
        return tables

    def get_schema(self, id: str, table_name: str) -> Dict:
        url = urllib.parse.urljoin(
            self.url_base,
            f"/api/{API_VERSION}sources/{id}/schema?table_name={table_name}",
        )
        return self.get(url)

    def update_profiler_config(self, id: str, table_uuid: str, data: Dict) -> Dict:
        url = urllib.parse.urljoin(
            self.url_base,
            f"/api/{API_VERSION}/sources/{id}/profile/tables/{table_uuid}/profiler-config",
        )
        return self.put(url, data)

    def trigger_source(self, id: str) -> Dict:
        source = self.get_source(id)
        if not source["config"].get("triggered", {}).get("enabled"):
            return {"error": "source is not configured for triggers"}

        url = urllib.parse.urljoin(
            self.url_base, f"/api/{API_VERSION}/sources/{id}/trigger"
        )
        return self.put(url, data={})
