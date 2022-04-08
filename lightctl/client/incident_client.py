import logging
import urllib.parse
from typing import Dict
from uuid import UUID

from lightctl.client.base_client import BaseClient

logger = logging.getLogger(__name__)


class IncidentClient(BaseClient):
    def incidents_url(self, workspace_id) -> str:
        return urllib.parse.urljoin(
            self.url_base, f"/api/v0/ws/{workspace_id}/incidents"
        )

    def get_incidents(
        self, workspace_id: str, monitor_id: str, start_ts: int, end_ts: int
    ) -> Dict:
        assert UUID(workspace_id)
        assert UUID(monitor_id)
        assert start_ts is not None
        assert end_ts is not None
        assert start_ts < end_ts

        url = (
            self.incidents_url(workspace_id)
            + f"?start_ts={start_ts}&end_ts={end_ts}&filter_uuids={monitor_id}"
        )
        return self.get(url).get("data")
