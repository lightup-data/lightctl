import os

__version__ = "v1alpha"


# TODO: [prod] remove credential
def get_url_base():
    return os.environ.get("LIGHTUP_URL_BASE", "https://app.stage.lightup.ai")


def get_username():
    return os.environ.get("LIGHTUP_USERNAME", "automaton")


def get_password():
    return os.environ.get("LIGHTUP_PASSWORD", "fFlIYFDF^eKs0Ab@jjhW8WTjfkMW%H7!")


# TODO: use config file and cache session

URL_BASE = get_url_base()
USERNAME = get_username()
PASSWORD = get_password()
