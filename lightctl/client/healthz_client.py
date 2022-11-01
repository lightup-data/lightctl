import logging
import urllib.parse
from typing import Dict

from lightctl.client.base_client import BaseClient

logger = logging.getLogger(__name__)


class HealthzClient(BaseClient):
    @property
    def healthz_url(self) -> str:
        return urllib.parse.urljoin(self.url_base, f"/api/v0/healthz/")

    def get_healthz_info(self) -> Dict:
        return self.get(self.healthz_url)
