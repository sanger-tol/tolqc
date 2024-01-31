# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import os

from flask import Flask

from tol.api_base2 import data_blueprint, system_blueprint
from tol.api_base2.misc import quick_and_dirty_auth
from tol.core import core_data_object
from tol.sql import create_sql_datasource

import tolqc.assembly_models
import tolqc.sample_data_models

from .reports import reports_blueprint


def models_list():
    return [
        *tolqc.assembly_models.models_list(),
        *tolqc.sample_data_models.models_list(),
    ]


def application(session_factory=None, database_factory=None):
    """
    The `session_factory` and `database_factory` arguments are used during
    testing.
    """
    app = Flask(__name__)

    api_path = os.getenv('API_PATH', '/api/v1')

    ds_args = {}
    if database_factory:
        ds_args['database_factory'] = database_factory

    # Tol QC endpoints
    tolqc_ds = create_sql_datasource(
        models=models_list(),
        db_uri=os.getenv('DB_URI'),
        **ds_args,
    )
    authenticator = quick_and_dirty_auth(os.getenv('API_TOKEN'))

    # Data endpoints
    blueprint_data_tolqc = data_blueprint(
        tolqc_ds,
        authenticator=authenticator,
    )
    app.register_blueprint(
        blueprint_data_tolqc,
        name='tolqc',
        url_prefix=api_path,
    )
    core_data_object(tolqc_ds)

    # Reports
    blueprint_reports = reports_blueprint(
        db_uri=os.getenv('DB_URI'),
        session_factory=session_factory,
        authenticator=authenticator,
        url_prefix='/reports',
    )
    app.register_blueprint(blueprint_reports)

    # System endpoints
    blueprint_system = system_blueprint(tolqc_ds)
    app.register_blueprint(
        blueprint_system,
        url_prefix=api_path + '/system',
    )

    return app
