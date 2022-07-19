import uuid

from lightctl.client.workspace_client import WorkspaceClient


class TestWorkspaceClient:
    def test_list_workspaces_and_create_and_delete_workspace(
        self, fixture_workspace_client: WorkspaceClient
    ):
        workspaces = fixture_workspace_client.list_workspaces()
        res = fixture_workspace_client.create_workspace(
            f"lightctl-ws-test-{uuid.uuid4()}"
        )
        assert res["uuid"] not in [ws["uuid"] for ws in workspaces]
        workspaces = fixture_workspace_client.list_workspaces()
        assert res in workspaces
