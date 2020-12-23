import logging
import urllib.parse

from lightctl.client.base_client import BaseClient

logger = logging.getLogger(__name__)


class HealthzClient(BaseClient):
    @property
    def healthz_url(self):
        return urllib.parse.urljoin(self.url_base, "/api/v1alpha/healthz/")

    def get_healthz_info(self):
        return self.get(self.healthz_url)
