from typing import Dict
from uuid import uuid4

import pytest

from lightctl.client.user_client import UserClient


class TestUserClient:
    @pytest.fixture
    def fixture_user_client(self):
        return UserClient()

    def test_add_update_remove_user(
        self, fixture_workspace: Dict, fixture_user_client: UserClient
    ):
        test_user = f"testerlightup+{uuid4()}@gmail.com"
        workspace_id = fixture_workspace["uuid"]

        res = fixture_user_client.list_users(workspace_id)
        assert len(res) == 0

        # add user to workspace
        user_res = fixture_user_client.add_user_to_workspace(
            fixture_workspace["uuid"], test_user, "viewer"
        )
        assert user_res["username"] == test_user
        assert user_res["role"].get("name") == "viewer"

        res = fixture_user_client.list_users(workspace_id)
        assert len(res) == 1
        assert test_user == res[0]["username"]
        assert res[0]["role"]["name"] == "viewer"

        # update user in workspace
        fixture_user_client.update_user_role(workspace_id, test_user, "editor")

        res = fixture_user_client.list_users(workspace_id)
        assert len(res) == 1
        assert test_user == res[0]["username"]
        assert res[0]["role"]["name"] == "editor"

        # remove user
        fixture_user_client.remove_user_from_workspace(
            workspace_id, user_res["username"]
        )

        res = fixture_user_client.list_users(workspace_id)
        assert len(res) == 0
