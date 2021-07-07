import logging
import urllib.parse
from typing import List, Optional

from lightctl.client.base_client import BaseClient
from lightctl.config import API_VERSION

logger = logging.getLogger(__name__)


class RuleClient(BaseClient):
    @property
    def rules_url(self):
        return urllib.parse.urljoin(self.url_base, f"/api/{API_VERSION}/rules/")

    def list_rules(self):
        res = self.get(self.rules_url)
        return res.get("data", [])

    def get_rule(self, id: str):
        url = urllib.parse.urljoin(self.rules_url, id)
        rule = self.get(url)
        return rule

    # TODO: [v1] support query in backend
    def get_rule_by_name(self, name):
        # name is not unique
        rule_list = []
        rules = self.list_rules()
        for rule in rules:
            if rule["name"] == name:
                rule_list.append(rule)
        return rule_list

    def create_rule(self, data):
        return self.post(self.rules_url, data)

    def update_rule(self, id, data):
        url = urllib.parse.urljoin(self.rules_url, id)
        return self.put(url, data)

    def delete_rule(self, id):
        self.delete(self.rules_url, id)

    def get_rules_by_metric(self, metric_uuid) -> List[dict]:
        rules_in_metric = []

        rules = self.list_rules()
        for rule in rules:
            if metric_uuid in rule["config"]["metrics"]:
                rules_in_metric.append(rule)
        return rules_in_metric

    def last_processed_timestamp(self, id) -> Optional[float]:
        rule = self.get_rule(id)
        if rule is None:
            return None
        return rule["status"]["lastSampleTs"]
