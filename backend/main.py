#!/usr/bin/env python3
import connexion
from flask_cors import CORS

# Uses the connexion library to create a Flask app implmenting the OpenAPI
# specification (../apis/paios/openapi.yaml), calling the python functions
# in operationId (eg api.get_asset_by_id in api.py)

app = connexion.App(__name__, specification_dir='../apis/paios/')
CORS(app.app, expose_headers='X-Total-Count')

app.add_api('openapi.yaml')

if __name__ == '__main__':
    app.run(port=3000)