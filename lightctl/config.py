import os
from pathlib import Path

API_VERSION = "v1"

LIGHTCTL_TOKEN_CACHE_PATH = os.environ.get(
    "LIGHTCTL_TOKEN_CACHE_PATH",
    os.path.join(str(Path.home()), ".lightup", ".access-token-cache"),
)

LIGHTCTL_CREDENTIAL_PATH = os.environ.get(
    "LIGHTCTL_CREDENTIAL_PATH",
    os.path.join(str(Path.home()), ".lightup", "credential"),
)

LIGHTCTL_DEFAULT_WORKSPACE = os.environ.get(
    "LIGHTCTL_DEFAULT_WORKSPACE", "497d2c3e-2e24-47ec-b33a-dcf3999062a7"
)
