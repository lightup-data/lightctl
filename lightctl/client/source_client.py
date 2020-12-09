import logging
import os
import urllib.parse

from lightctl.client.base_client import BaseClient

logger = logging.getLogger(__name__)


class SourceClient(BaseClient):
    @property
    def sources_url(self):
        return urllib.parse.urljoin(self.url_base, "/api/v0/sources/")

    def list_sources(self):
        return self.get(self.sources_url)

    def get_source(self, id_: str):
        url = urllib.parse.urljoin(self.sources_url, id_)
        return self.get(url)

    def get_source_by_name(self, name):
        sources = self.list_sources()
        for source in sources:
            if source["name"] == name:
                return source
        return None

    def create_source(self, data):
        return self.post(self.sources_url, data)

    def delete_source(self, id_):
        self.delete(self.sources_url, id_)

    def inspect(self, data):
        urllib.parse.urljoin(self.url_base, "/api/v0/sources-inspection/")
        return self.post(self.sources_url, data)
