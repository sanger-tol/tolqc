# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import os
import logging


def _get_environment_env():
    deployment_environment = os.getenv("ENVIRONMENT", "")
    if deployment_environment != "":
        return deployment_environment

    # if unset, assume dev
    logging.warning("$ENVIRONMENT is unset - assuming a 'dev' environment")
    return "dev"


def set_config(app, encoder):
    app.config['DEPLOYMENT_ENVIRONMENT'] = _get_environment_env()
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['RESTX_JSON'] = {'cls': encoder}
