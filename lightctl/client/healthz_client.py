import logging
import urllib.parse

from lightctl.client.base_client import BaseClient
from lightctl.config import URL_BASE

logger = logging.getLogger(__name__)


class HealthzClient(BaseClient):
    @property
    def healthz_url(self):
        return urllib.parse.urljoin(URL_BASE, "/api/v1/healthz/")

    def get_healthz_info(self):
        return self.get(self.healthz_url)
