import logging
import urllib.parse
from typing import Dict

from lightctl.client.base_client import BaseClient

logger = logging.getLogger(__name__)


class IncidentClient(BaseClient):
    @property
    def incident_url(self) -> str:
        return urllib.parse.urljoin(self.url_base, f"/api/v0/incidents")

    def get_incidents(self, monitor_id: str, start_ts: int, end_ts: int) -> Dict:
        assert monitor_id is not None
        assert start_ts is not None
        assert end_ts is not None
        assert start_ts < end_ts

        url = (
            self.incident_url
            + f"?start_ts={start_ts}&end_ts={end_ts}&filter_uuids={monitor_id}"
        )
        return self.get(url).get("data")
