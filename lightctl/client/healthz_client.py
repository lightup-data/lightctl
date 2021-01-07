import logging
import urllib.parse

from lightctl.client.base_client import BaseClient
from lightctl.config import API_VERSION, URL_BASE

logger = logging.getLogger(__name__)


class HealthzClient(BaseClient):
    @property
    def healthz_url(self):
        return urllib.parse.urljoin(URL_BASE, f"/api/{API_VERSION}/healthz/")

    def get_healthz_info(self):
        return self.get(self.healthz_url)
