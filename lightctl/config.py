import os
from pathlib import Path

__version__ = "v1"

URL_BASE = os.environ.get("LIGHTUP_URL_BASE", "https://app.stage.lightup.ai")

ACCESS_TOKEN_CACHE_FILE_PATH = os.path.join(
    str(Path.home()), ".lightup", "cached-cli-access-token"
)

CREDENTIAL_FILE_PATH = os.path.join(str(Path.home()), ".lightup", "cli-credential")
