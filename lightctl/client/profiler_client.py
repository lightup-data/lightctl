import logging
import urllib.parse
from typing import Dict

from lightctl.client.base_client import BaseClient
from lightctl.config import API_VERSION

logger = logging.getLogger(__name__)


class ProfilerClient(BaseClient):
    def profiler_base_url(self, workspace_id: str, source_uuid) -> str:
        return urllib.parse.urljoin(
            self.url_base,
            f"/api/{API_VERSION}/ws/{workspace_id}/sources/{source_uuid}/profile/",
        )

    # schema level functions
    def schema_uuid_from_schema_name(
        self, workspace_id: str, source_uuid: str, schema_name: str
    ) -> str:
        base_url = self.profiler_base_url(workspace_id, source_uuid)
        url = urllib.parse.urljoin(base_url, "schemas")

        schemas = self.get(url)
        for schema in schemas["data"]:
            if schema["name"] == schema_name:
                return schema["uuid"]

    def get_schema_profiler_config(
        self, workspace_id: str, source_uuid: str, schema_uuid: str
    ) -> Dict:
        base_url = self.profiler_base_url(workspace_id, source_uuid)

        url = urllib.parse.urljoin(
            base_url,
            f"schemas/{schema_uuid}/profiler-config",
        )
        return self.get(url)

    def update_schema_profiler_config(
        self, workspace_id: str, source_uuid: str, schema_uuid: str, data: Dict
    ) -> Dict:
        base_url = self.profiler_base_url(workspace_id, source_uuid)

        url = urllib.parse.urljoin(base_url, f"schemas/{schema_uuid}/profiler-config")
        return self.put(url, data)

    # table level functions
    def table_uuid_from_table_name(
        self, workspace_id: str, source_uuid: str, table_name: str
    ) -> str:
        return ""

    def get_table_profiler_config(
        self, workspace_id: str, source_uuid: str, schema_uuid: str
    ) -> Dict:
        base_url = self.profiler_base_url(workspace_id, source_uuid)

        url = urllib.parse.urljoin(
            base_url,
            f"schemas/{schema_uuid}/profiler-config",
        )
        return self.get(url)

    def update_table_profiler_config(
        self, workspace_id: str, source_uuid: str, table_uuid: str, data: Dict
    ) -> Dict:
        base_url = self.profiler_base_url(workspace_id, source_uuid)

        url = urllib.parse.urljoin(base_url, f"tables/{table_uuid}/profiler-config")
        return self.put(url, data)

    # column level functions
    def column_uuid_from_column_name(
        self, workspace_id: str, source_uuid: str, table_uuid: str, column_name: str
    ) -> str:
        return ""

    def get_column_profiler_config(
        self, workspace_id: str, source_uuid: str, table_uuid: str, column_uuid: str
    ) -> Dict:
        base_url = self.profiler_base_url(workspace_id, source_uuid)

        url = urllib.parse.urljoin(
            base_url, f"tables/{table_uuid}/columns/{column_uuid}/profiler-config"
        )
        return self.get(url)

    def update_column_profiler_config(
        self,
        workspace_id: str,
        source_uuid: str,
        table_uuid: str,
        column_uuid: str,
        data: Dict,
    ) -> Dict:
        base_url = self.profiler_base_url(workspace_id, source_uuid)

        url = urllib.parse.urljoin(
            base_url, f"tables/{table_uuid}/columns/{column_uuid}/profiler-config"
        )
        return self.put(url, data)
