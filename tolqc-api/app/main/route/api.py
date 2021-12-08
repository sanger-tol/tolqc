# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask import Blueprint
from flask_restx import Api

from main.config import deployment_environment
from main.resource import centre_namespace, environment_namespace

def _get_environment_string():
    if deployment_environment == 'production':
        return ""
    return f" ({deployment_environment})"

def _setup_api(blueprint):
    api = Api(
        blueprint,
        doc='/ui',
        title=f"Tree of Life Quality Control{_get_environment_string()}"
    )
    api.add_namespace(centre_namespace)
    api.add_namespace(environment_namespace)

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
_setup_api(blueprint)
