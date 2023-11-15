#!/usr/bin/env bash

# Usage: source dev.sh

# go to right folder
REPO_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "${REPO_DIR}" || exit

# exit previous venv if any
deactivate || true

# set python dev env
python -m venv .lightctl-venv
source .lightctl-venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# install pre-commit, use it Black as in .pre-commit-config.yaml
python -m pip install pre-commit
pre-commit install

export PYTHONPATH=$(pwd):$PYTHONPATH
