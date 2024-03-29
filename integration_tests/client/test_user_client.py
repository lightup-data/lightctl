import uuid

import pytest

from lightctl.client.user_client import UserClient
from lightctl.util import LightupException

TEST_EMAIL_ADDRESS = "fillmein+{}@xyz.com"


class TestUserClient:
    @pytest.fixture
    def fixture_user_client(self) -> UserClient:
        return UserClient()

    @pytest.fixture
    def fixture_user(self, fixture_user_client) -> str:
        user_id = TEST_EMAIL_ADDRESS.format(str(uuid.uuid4()))
        fixture_user_client.add_app_user(user_id, "app_admin")
        yield user_id
        fixture_user_client.delete_app_user(user_id)

    def test_update_app_user_role(
        self, fixture_user_client: UserClient, fixture_user: str
    ):
        app_users = fixture_user_client.list_app_users()
        assert fixture_user in [user["username"] for user in app_users]

        app_user = fixture_user_client.get_app_user(fixture_user)
        assert app_user["role"]["name"] == "app_admin"

        fixture_user_client.update_app_user_role(fixture_user, "app_viewer")
        app_user = fixture_user_client.get_app_user(fixture_user)
        assert app_user["role"]["name"] == "app_viewer"

    def test_add_update_remove_user(
        self,
        fixture_workspace: dict,
        fixture_user_client: UserClient,
        fixture_user: str,
    ):
        test_user = fixture_user
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

    def test_update_app_user_detail(
        self,
        fixture_user_client: UserClient,
    ):
        user_id = TEST_EMAIL_ADDRESS
        try:
            fixture_user_client.delete_app_user(user_id)
        except LightupException:
            pass
        fixture_user_client.add_app_user(user_id, "app_viewer")
        app_user = fixture_user_client.get_app_user(user_id)
        assert app_user["expiration_timestamp"] is None

        fixture_user_client.update_app_user_detail(
            user_id, {"expirationTimestamp": 1704067200}
        )

        app_user = fixture_user_client.get_app_user(user_id)
        assert app_user["expiration_timestamp"] == 1704067200

        # clean up
        fixture_user_client.delete_app_user(user_id)
