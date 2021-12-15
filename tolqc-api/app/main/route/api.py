# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask import Blueprint
from flask_restx import Api

from main.auth import authorizations
from main.resource import api_centre, api_environment
from main.schema import CentreSchema


def _get_environment_string(app):
    environment = app.config['DEPLOYMENT_ENVIRONMENT']
    if environment == 'production':
        return ""
    return f" ({environment})"

def _get_path_from_schema(schema):
    return f"/{schema.get_type()}"

def _setup_api(blueprint, app):
    api = Api(
        blueprint,
        doc='/ui',
        title=f"Tree of Life Quality Control{_get_environment_string(app)}",
        authorizations=authorizations
    )
    api.add_namespace(api_centre, path=_get_path_from_schema(CentreSchema))
    api.add_namespace(api_environment, path='/environments')


def init_blueprint(app):
    blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
    _setup_api(blueprint, app)
    return blueprint
