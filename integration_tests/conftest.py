import uuid

import pytest

from lightctl.client.workspace_client import WorkspaceClient


@pytest.fixture
def fixture_workspace_client() -> WorkspaceClient:
    workspace_client = WorkspaceClient()
    # do not run the test on production clusters
    assert (
        workspace_client.credential["data"]["server"] == "https://app.stage.lightup.ai"
    )
    return workspace_client


@pytest.fixture
def fixture_workspace(fixture_workspace_client: WorkspaceClient):
    # TODO: this workspace needs to be torn down at the end of the test.
    res = fixture_workspace_client.create_workspace(f"lightctl-test-{uuid.uuid4()}")
    return res
