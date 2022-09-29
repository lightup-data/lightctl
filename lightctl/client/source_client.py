import logging
import urllib.parse
from typing import Dict, List
from uuid import UUID

from lightctl.client.base_client import BaseClient
from lightctl.config import API_VERSION

logger = logging.getLogger(__name__)


class SourceClient(BaseClient):
    def sources_url(self, workspace_id: str) -> str:
        return urllib.parse.urljoin(
            self.url_base, f"/api/{API_VERSION}/ws/{workspace_id}/sources/"
        )

    def list_sources(self, workspace_id: str) -> List[Dict]:
        return self.get(self.sources_url(workspace_id))

    def get_source(self, workspace_id: str, id: UUID) -> Dict:
        url = urllib.parse.urljoin(self.sources_url(workspace_id), f"{id}")
        return self.get(url)

    def get_source_by_name(self, workspace_id: str, name: str) -> List[Dict]:
        ret_sources = []
        sources = self.list_sources(workspace_id)
        for source in sources:
            if source["metadata"]["name"] == name:
                ret_sources.append(source)
        return ret_sources

    def create_source(self, workspace_id: str, data: Dict) -> Dict:
        return self.post(self.sources_url(workspace_id), data)

    def update_source(self, workspace_id: str, id: UUID, data: Dict) -> Dict:
        url = urllib.parse.urljoin(self.sources_url(workspace_id), f"{id}")
        return self.put(url, data)

    def delete_source(self, workspace_id: str, id: UUID) -> Dict:
        self.delete(self.sources_url(workspace_id), f"{id}")

    def inspect(self, workspace_id: str, data: Dict) -> Dict:
        url = urllib.parse.urljoin(
            self.sources_url(workspace_id), "/sources/inspection"
        )
        return self.post(url, data, expected_status=200)

    def list_columns(self, workspace_id: str, id: UUID, table_id: UUID) -> List[Dict]:
        url = urllib.parse.urljoin(
            self.sources_url(workspace_id), f"{id}/profile/tables/{table_id}/columns"
        )
        columns = self.get(url)
        return columns

    def get_column(
        self, workspace_id: str, id: UUID, table_id: UUID, column_id: UUID
    ) -> Dict:
        url = urllib.parse.urljoin(
            self.sources_url(workspace_id),
            f"{id}/profile/tables/{table_id}/columns/{column_id}",
        )
        column = self.get(url)
        return column

    def list_tables(self, workspace_id: str, id: UUID) -> List[Dict]:
        url = urllib.parse.urljoin(
            self.sources_url(workspace_id), f"{id}/profile/tables"
        )
        tables = self.get(url)
        return tables["data"]

    def get_table(self, workspace_id: str, id: UUID, table_id: UUID) -> Dict:
        url = urllib.parse.urljoin(
            self.sources_url(workspace_id), f"{id}/profile/tables/{table_id}"
        )
        table = self.get(url)
        return table

    def get_table_schema(self, workspace_id: str, id: UUID, table_name: str) -> Dict:
        url = urllib.parse.urljoin(
            self.sources_url(workspace_id),
            f"{id}/schema?table_name={table_name}",
        )
        return self.get(url)

    def list_schemas(self, workspace_id: str, id: UUID) -> List[Dict]:
        url = urllib.parse.urljoin(
            self.sources_url(workspace_id), f"{id}/profile/schemas"
        )
        schemas = self.get(url)
        return schemas["data"]

    def get_schema(self, workspace_id: str, id: UUID, schema_id: UUID) -> Dict:
        url = urllib.parse.urljoin(
            self.sources_url(workspace_id), f"{id}/profile/schemas/{schema_id}"
        )
        schema = self.get(url)
        return schema

    def update_profiler_config(
        self, workspace_id: str, id: UUID, table_uuid: str, data: Dict
    ) -> Dict:
        url = urllib.parse.urljoin(
            self.sources_url(workspace_id),
            f"{id}/profile/tables/{table_uuid}/profiler-config",
        )
        return self.put(url, data)

    def trigger_source(self, workspace_id: str, id: UUID, data: Dict) -> Dict:
        url = urllib.parse.urljoin(self.sources_url(workspace_id), f"{id}/trigger")
        return self.post(url, data=data)

    def activate_source(self, workspace_id: str, id: UUID, enable: bool = True):
        source = self.get_source(workspace_id, id)
        profiler_config = source["config"]["profiler"]
        if profiler_config["enabled"] == enable:
            return profiler_config

        profiler_config["enabled"] = enable
        url = urllib.parse.urljoin(
            self.sources_url(workspace_id), f"{id}/profile/profiler-config"
        )
        return self.put(url, data=profiler_config)

    def activate_schema(
        self, workspace_id: str, id: UUID, schema_id: UUID, enable: bool = True
    ):
        schema = self.get_schema(workspace_id, id, schema_id)
        profiler_config = schema["profilerConfig"]
        if profiler_config["enabled"] == enable:
            return profiler_config

        profiler_config["enabled"] = enable
        url = urllib.parse.urljoin(
            self.sources_url(workspace_id),
            f"{id}/profile/schemas/{schema_id}/profiler-config",
        )
        return self.put(url, data=profiler_config)

    def activate_table(
        self, workspace_id: str, id: UUID, table_id: UUID, enable: bool = True
    ):
        table = self.get_table(workspace_id, id, table_id)
        profiler_config = table["profilerConfig"]
        if profiler_config["enabled"] == enable:
            return profiler_config

        profiler_config["enabled"] = enable
        url = urllib.parse.urljoin(
            self.sources_url(workspace_id),
            f"{id}/profile/tables/{table_id}/profiler-config",
        )
        return self.put(url, data=profiler_config)

    def activate_column(
        self,
        workspace_id: str,
        id: UUID,
        table_id: UUID,
        column_id: UUID,
        enable: bool = True,
    ):
        column = self.get_column(workspace_id, id, table_id, column_id)
        profiler_config = column["profilerConfig"]
        if profiler_config["enabled"] == enable:
            return profiler_config

        profiler_config["enabled"] = enable
        url = urllib.parse.urljoin(
            self.sources_url(workspace_id),
            f"{id}/profile/tables/{table_id}/columns/{column_id}/profiler-config",
        )
        return self.put(url, data=profiler_config)
