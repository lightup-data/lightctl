import logging
import urllib.parse
from typing import Dict, List, Optional

from lightctl.client.base_client import BaseClient
from lightctl.config import API_VERSION

logger = logging.getLogger(__name__)


class RuleClient(BaseClient):
    @property
    def rules_url(self) -> str:
        return urllib.parse.urljoin(self.url_base, f"/api/{API_VERSION}/rules/")

    def list_rules(self) -> List[Dict]:
        res = self.get(self.rules_url)
        return res.get("data", [])

    def get_rule(self, id: str) -> Dict:
        url = urllib.parse.urljoin(self.rules_url, id)
        rule = self.get(url)
        return rule

    def get_rule_by_name(self, name) -> List[Dict]:
        url = urllib.parse.urljoin(self.rules_url, f"?names={name}")
        # name is not unique
        return self.get(url)

    def create_rule(self, data) -> Dict:
        return self.post(self.rules_url, data)

    def update_rule(self, id, data) -> Dict:
        url = urllib.parse.urljoin(self.rules_url, id)
        return self.put(url, data)

    def delete_rule(self, id):
        self.delete(self.rules_url, id)

    def get_rules_by_metric(self, metric_uuid) -> List[Dict]:
        url = urllib.parse.urljoin(self.rules_url, f"?metric_uuids={metric_uuid}")
        return self.get(url)

    def last_processed_timestamp(self, id) -> Optional[float]:
        rule = self.get_rule(id)
        if rule is None:
            return None
        return rule["status"]["lastSampleTs"]
