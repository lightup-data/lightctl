#!/usr/bin/env bash

# Usage: ./deploy.sh

# Requirement
# - we are using s3pypi that use S3 to distribute python package. See https://github.com/novemberfiveco/s3pypi
# - bucket is managed by aurora/terraform
# - pip install s3pypi

BUCKET=pypi.lightup.ai
SECRET=poc

printf "This script package lightctl and upload to s3\n"
printf "To install, use \n"
printf "pip install lightctl --find-links https://s3-us-west-2.amazonaws.com/%s/%s/lightctl/index.html\n" ${BUCKET} ${SECRET}

printf "Uploading package... \n"
s3pypi --bucket ${BUCKET} --secret ${SECRET} --private
