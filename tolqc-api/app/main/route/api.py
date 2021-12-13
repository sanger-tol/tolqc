# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask import Blueprint
from flask_restx import Api

from main.swagger import centre_namespace, environment_namespace, \
                          run_namespace, authorizations


def _get_environment_string(app):
    environment = app.config['DEPLOYMENT_ENVIRONMENT']
    if environment == 'production':
        return ""
    return f" ({environment})"


def _setup_api(blueprint, app):
    api = Api(
        blueprint,
        doc='/ui',
        title=f"Tree of Life Quality Control{_get_environment_string(app)}",
        authorizations=authorizations
    )
    api.add_namespace(centre_namespace)
    api.add_namespace(environment_namespace)
    api.add_namespace(run_namespace)


def init_blueprint(app):
    blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
    _setup_api(blueprint, app)
    return blueprint
