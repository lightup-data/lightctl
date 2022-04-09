import uuid

from lightctl.client.workspace_client import WorkspaceClient


class TestWorkspaceClient:
    def test_list_workspaces_and_create_workspace(
        self, fixture_workspace_client: WorkspaceClient
    ):
        workspaces = fixture_workspace_client.list_workspaces()
        res = fixture_workspace_client.create_workspace(f"delete_me_{uuid.uuid4()}")
        assert res not in workspaces
        workspaces = fixture_workspace_client.list_workspaces()
        assert res in workspaces

    def test_workspace_delete(self, fixture_workspace_client):
        # not yet implemented
        pass
