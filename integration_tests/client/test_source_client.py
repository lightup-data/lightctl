import os
import uuid

import pytest

from lightctl.client.source_client import SourceClient


class TestSourceClient:
    @pytest.fixture
    def fixture_source_client(self) -> SourceClient:
        source_client = SourceClient()
        return source_client

    @staticmethod
    def get_source_dict() -> dict:
        source_dict: dict = {
            "metadata": {"name": f"Lightctl Test Databricks - {uuid.uuid4()}"},
            "config": {
                "connection": {
                    "type": "databricks",
                    "token": os.environ.get(
                        "LIGHTCTL_TEST_DATABRICKS_TOKEN", "replaceMeWithRealToken"
                    ),
                    "workspaceUrl": "dbc-e4e2fb19-633a.cloud.databricks.com",
                    "httpPath": "sql/protocolv1/o/6193792391218044/1013-024910-troys963",
                    "apiPort": 15001,
                    "dbname": "lightup_demo",
                },
                "profiler": {"enabled": True, "schemaList": ["lightup_demo"]},
            },
        }
        return source_dict

    def test_source_create_list_delete(
        self,
        fixture_workspace: dict,
        fixture_source_client: SourceClient,
    ):
        workspace_id = fixture_workspace["uuid"]

        res = fixture_source_client.list_sources(workspace_id)
        assert len(res) == 0

        source_dict = self.get_source_dict()
        res = fixture_source_client.create_source(workspace_id, source_dict)
        assert res["metadata"]["workspaceId"] == workspace_id
        assert res["metadata"]["name"] == source_dict["metadata"]["name"]

        res = fixture_source_client.list_sources(workspace_id)
        assert len(res) == 1
        assert res[0]["metadata"]["name"] == source_dict["metadata"]["name"]

        fixture_source_client.delete_source(workspace_id, res[0]["metadata"]["uuid"])
        res = fixture_source_client.list_sources(workspace_id)
        assert len(res) == 0
