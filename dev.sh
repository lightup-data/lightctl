#!/usr/bin/env bash

# Usage: source dev.sh

# go to right folder
REPO_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "${REPO_DIR}" || exit

# exit previous venv if any
deactivate || true

# set python dev env
python3 -m venv .lightctl-venv
source .lightctl-venv/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt

# install pre-commit, use it Black as in .pre-commit-config.yaml
pip3 install pre-commit
pre-commit install

export PYTHONPATH=$(pwd):$PYTHONPATH
