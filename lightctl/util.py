import json
import logging

import yaml

logger = logging.getLogger(__name__)


class CliPrinter:
    def __init__(self, use_json_format=False):
        self._use_json_format = use_json_format

    def print(self, obj):
        if self._use_json_format:
            print(json.dumps(obj, indent=4))
        else:
            print(yaml.dump(obj))


def check_status_code(r, expected=200):
    if r.status_code != expected:
        logger.debug(
            "Status: %s. Expected Status: %s. Error Text: %s",
            r.status_code,
            expected,
            r.text,
        )
        raise Exception(
            "Status: {}. Expected Status: {}. Error Text: {}.".format(
                r.status_code, expected, r.text
            )
        )
    return True
