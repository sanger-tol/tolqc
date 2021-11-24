#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import os
import logging
from flask import Blueprint, Flask
from flask_restx import Api

from main import encoder
from main.model import db
from main.resource import TolqcCentreResource, centre_namespace, \
                          EnvironmentResource, environment_namespace, \
                          TolqcRunResource, run_namespace


def _get_environment():
    deployment_environment = os.getenv("ENVIRONMENT", "")
    if deployment_environment != "":
        return deployment_environment

    # if unset, assume dev
    logging.warning("$ENVIRONMENT is unset - assuming a 'dev' environment")
    return "dev"


def _get_environment_string(app):
    environment = app.config["DEPLOYMENT_ENVIRONMENT"]
    if environment == 'production':
        return ""
    return f" ({environment})"


def _setup_api(blueprint, app):
    api = Api(
        blueprint,
        doc='/ui',
        title=f"Tree of Life Quality Control{_get_environment_string(app)}"
    )
    api.add_namespace(centre_namespace)
    api.add_namespace(run_namespace)
    api.add_namespace(environment_namespace)


def _add_resources():
    centre_namespace.add_resource(TolqcCentreResource, '/<int:id>')
    run_namespace.add_resource(TolqcRunResource, '/<int:id>')
    environment_namespace.add_resource(EnvironmentResource, '')


def application():
    app = Flask(__name__)
    app.config["DEPLOYMENT_ENVIRONMENT"] = _get_environment()
    blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
    _setup_api(blueprint, app)
    _add_resources()
    app.register_blueprint(blueprint)
    app.json_encoder = encoder.JSONEncoder
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app
