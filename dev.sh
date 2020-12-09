#!/usr/bin/env bash

# install pre-commit, use it Black as in .pre-commit-config.yaml
pip3 install pre-commit
pre-commit install

# set python dev env
pip3 install -r requirements.txt
export PYTHONPATH=$(pwd):$PYTHONPATH
