import logging
import urllib.parse
from typing import Dict, Optional
from uuid import UUID

from lightctl.client.base_client import BaseClient

logger = logging.getLogger(__name__)


class IncidentClient(BaseClient):
    def incidents_url(self, workspace_id) -> str:
        return urllib.parse.urljoin(
            self.url_base, f"/api/v0/ws/{workspace_id}/incidents/"
        )

    def list_incidents(
        self,
        workspace_id: str,
        start_ts: int,
        end_ts: int,
        monitor_id: Optional[str] = None,
    ) -> Dict:
        assert UUID(workspace_id)
        if monitor_id:
            assert UUID(monitor_id)
            monitor_id = f"&filter_uuids={monitor_id}"
        else:
            monitor_id = ""
        assert start_ts is not None
        assert end_ts is not None
        assert start_ts < end_ts

        url = (
            self.incidents_url(workspace_id)
            + f"?start_ts={start_ts}&end_ts={end_ts}{monitor_id}"
        )
        return self.get(url).get("data")

    def update_incident_status(self, workspace_id: str, id: str, status: str) -> Dict:
        incident_status_map = {
            "unviewed": 1,
            "viewed": 2,
            "rejected": 3,
            "submitted": 4,
            "closed": 5,
        }
        incident_status = incident_status_map.get(status)
        assert incident_status is not None, f"invalid incident status '{status}'"
        url = urllib.parse.urljoin(self.incidents_url(workspace_id), f"{id}")
        return self.patch(url, data={"status": incident_status})

    def update_incident_validation(
        self, workspace_id: str, id: str, status: str
    ) -> Dict:
        validation_status = status.lower()
        assert validation_status in [
            "running",
            "canceling",
        ], f"invalid validation status '{status}"
        url = urllib.parse.urljoin(self.incidents_url(workspace_id), f"{id}")
        return self.patch(url, data={"validation": {"status": validation_status}})
