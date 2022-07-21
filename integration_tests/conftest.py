import uuid

import pytest

from lightctl.client.workspace_client import WorkspaceClient


@pytest.fixture(scope="session")
def fixture_workspace_client() -> WorkspaceClient:
    workspace_client = WorkspaceClient()
    # do not run the test on production clusters
    assert (
        workspace_client.credential["data"]["server"] == "https://app.stage.lightup.ai"
    )
    return workspace_client


@pytest.fixture(scope="session")
def fixture_workspace(fixture_workspace_client: WorkspaceClient):
    ws = f"lightctl-test-{uuid.uuid4()}"
    res = fixture_workspace_client.create_workspace(ws)
    yield res
    fixture_workspace_client.delete_workspace(res["uuid"])
