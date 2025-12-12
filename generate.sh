#!/bin/bash
source .venv/bin/activate
openapi-python-client generate --path ../maxapi/static/api/spec.yml --overwrite --meta uv --output-path generated
rm -rf ./maxapi_python
mv ./generated/max_api_client ./maxapi_python
rm -rf ./generated