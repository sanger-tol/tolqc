# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import os

from flask import Flask

from tol.api_base2 import data_blueprint, system_blueprint
from tol.core import core_data_object
from tol.sql import create_sql_datasource

import tolqc.assembly_models
import tolqc.sample_data_models
from tolqc.json import JSONDateTimeProvider
from tolqc.loaders import loaders_blueprint
from tolqc.reports import reports_blueprint


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
    app.json = JSONDateTimeProvider(app)

    api_path = os.getenv('API_PATH', '/api/v1')
    db_uri = os.getenv('DB_URI')

    ds_args = {}
    if database_factory:
        ds_args['database_factory'] = database_factory

    # Tol QC endpoints
    tolqc_ds = create_sql_datasource(
        models=models_list(),
        db_uri=db_uri,
        **ds_args,
    )

    # Data endpoints
    blueprint_data_tolqc = data_blueprint(tolqc_ds)
    app.register_blueprint(
        blueprint_data_tolqc,
        name='tolqc',
        url_prefix=api_path,
    )
    core_data_object(tolqc_ds)

    # Reports
    blueprint_reports = reports_blueprint(
        db_uri=db_uri,
        session_factory=session_factory,
        url_prefix='/report',
    )
    app.register_blueprint(blueprint_reports)

    # Data loaders
    blueprint_loaders = loaders_blueprint(
        db_uri=db_uri,
        session_factory=session_factory,
        url_prefix='/loader',
    )
    app.register_blueprint(blueprint_loaders)

    # System endpoints
    blueprint_system = system_blueprint(tolqc_ds)
    app.register_blueprint(
        blueprint_system,
        url_prefix=api_path + '/system',
    )

    return app