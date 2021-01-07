import logging
import urllib.parse

from lightctl.client.base_client import BaseClient
from lightctl.config import API_VERSION, URL_BASE

logger = logging.getLogger(__name__)


class RuleClient(BaseClient):
    @property
    def rules_url(self):
        return urllib.parse.urljoin(URL_BASE, f"/api/{API_VERSION}/rules/")

    def list_rules(self):
        return self.get(self.rules_url)

    def get_rule(self, id: str):
        url = urllib.parse.urljoin(self.rules_url, id)
        return self.get(url)

    # TODO: [v1] support query in backend
    def get_rule_by_name(self, name):
        rules = self.list_rules()
        for rule in rules:
            if rule["name"] == name:
                return rule
        return None

    def create_rule(self, data):
        return self.post(self.rules_url, data)

    def delete_rule(self, id):
        self.delete(self.rules_url, id)
