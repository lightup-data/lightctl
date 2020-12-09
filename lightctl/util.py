import json
import logging

import yaml

logger = logging.getLogger(__name__)


def cli_print(obj, is_json=False):
    if not is_json:
        print(yaml.dump(obj))
    else:
        print(json.dumps(obj, indent=4))


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
