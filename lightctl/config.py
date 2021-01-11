import os
from pathlib import Path

__version__ = "0.1.0"

API_VERSION = "v1"

ACCESS_TOKEN_CACHE_FILE_PATH = os.path.join(
    str(Path.home()), ".lightup", ".access-token-cache"
)

CREDENTIAL_FILE_PATH = os.environ.get(
    "LIGHTUP_API_CREDENTIAL",
    os.path.join(str(Path.home()), ".lightup", "credential"),
)
