import logging
import urllib.parse
from typing import Dict, List

from lightctl.client.base_client import BaseClient

logger = logging.getLogger(__name__)


class UserClient(BaseClient):
    """
    Helper functions for acessing workspace users

    Example:
        uc = UserClient()
        wc = WorkspaceClient()
        workspaces = wc.list_workspaces()
        workspace_name_to_update = "Revenue"
        workspace_to_update = [workspace for workspace in workspaces if workspace["name"] == workspace_name_to_update][0]
        uc.add_user_to_workspace(workspace_to_update["uuid"], "user@hello.com", "editor")

    """
    def app_users_url(self) -> str:
        """
        Returns:
           str: The app users endpoint, used for getting and modifying users
        """
        return urllib.parse.urljoin(self.url_base, "/api/v0/users/")

    def add_app_user(self, user_id: str, role: str) -> Dict:
        """
        Add a user to the app

        Args:
            user_id (str): User id (email) of user to be added to workspace
            role (str): Role of user when added to app. Legal roles are "app_admin", "app_editor", "app_viewer"

        Returns: 
            dict: A user object
        """
        assert role in ["app_admin", "app_editor", "app_viewer"]
        url = self.app_users_url()
        payload = {"email": user_id, "app_role": role}
        res = self.post(url, payload)
        return res

    def update_app_user_detail(self, user_id: str, payload: dict):
        """
        Update a user's detail in the app

        Args:
            user_id (str): User id (email) of user to be updated
            payload (dict): Properties to be modified
        Returns:
            dict: A user object
        """
        quoted_user = urllib.parse.quote_plus(user_id)
        url = urllib.parse.urljoin(self.app_users_url(), quoted_user)
        return self.patch(url, payload)

    def update_app_user_role(self, user_id: str, role: str):
        """
        Update a user's role in the app

        Args:
            user_id (str): User id (email) of user to be updated
            role (str): New role of user. Legal roles are "app_admin", "app_editor", "app_viewer"
        Returns:
            dict: A user object
        """
        assert role in ["app_admin", "app_editor", "app_viewer"]
        return self.update_app_user_detail(user_id, {"role": role})

    def delete_app_user(self, user_id: str):
        """
        Remove a user from the app

        Args:
            user_id (str): User id (email) of user to be removed

        Returns: 
            ??
        """
        quoted_user = urllib.parse.quote_plus(user_id)
        url = self.app_users_url()
        res = self.delete(url, quoted_user, force=True)
        return res

    def get_app_user(self, user_id: str):
        """
        Get an app user by user_id

        Args:
            user_id (str): User id (email) of user to be returned

        Returns: 
            dict: A user object
        """
        quoted_user = urllib.parse.quote_plus(user_id)
        url = urllib.parse.urljoin(self.app_users_url(), quoted_user)
        return self.get(url)

    def list_app_users(self) -> List[Dict]:
        """
        Get all users in the app

        Args:
            workspace_id (str): Workspace id

        Returns:
            list: a list of users
        """
        res = self.get(self.app_users_url())
        return res

    def users_url(self, workspace_id) -> str:
        """
        Returns:
           str: The workspace users endpoint, used for getting and modifying workspace users
        """
        return urllib.parse.urljoin(self.url_base, f"/api/v0/ws/{workspace_id}/users/")

    def add_user_to_workspace(self, workspace_id: str, user_id: str, role: str) -> Dict:
        """
        Add a user to a workspace

        Args:
            workspace_id (str): Workspace id
            user_id (str): User id (email) of user to be added to workspace
            role (str): Role of user when added to workspace. Legal roles are "viewer", "editor", "admin", and "observer" 

        Returns: 
            dict: A user object with role set to the user's role in the workspace
        """
        url = self.users_url(workspace_id)
        payload = {"email": user_id, "role": role}
        res = self.post(url, payload)
        return res

    def remove_user_from_workspace(self, workspace_id: str, user_id: str) -> Dict:
        """
        Remove user from a workspace

        Args:
            workspace_id (str): Workspace id
            user_id (str): User id (email) of user to be removed

        """
        url = self.users_url(workspace_id)
        quoted_user = urllib.parse.quote_plus(user_id)
        return self.delete(url, quoted_user, force=True)

    def update_user_role(self, workspace_id: str, user_id: str, role: str):
        """
        Update a user's role in a workspace

        Args:
            workspace_id (str): Workspace id
            user_id (str): User id (email) of user to be removed
            role (str): New role of user. Legal roles are "viewer", "editor", "admin", and "observer" 
        Returns:
            dict: A user object with role set to the user's role in the workspace
        """
        quoted_user = urllib.parse.quote_plus(user_id)
        url = urllib.parse.urljoin(self.users_url(workspace_id), quoted_user)
        payload = {"role": role}
        return self.patch(url, payload)

    def list_users(self, workspace_id: str) -> List[Dict]:
        """
        Get all users in the workspace

        Args:
            workspace_id (str): Workspace id

        Returns:
            list: a list of users
        """
        res = self.get(self.users_url(workspace_id))
        return res
