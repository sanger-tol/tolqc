# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import logging
import os

from flask import Flask, request

from sqlalchemy.event import remove
from sqlalchemy.orm import configure_mappers

from tol.api_base2 import data_blueprint, system_blueprint
from tol.api_base2.auth import basic_auth_inspector
from tol.core import core_data_object
from tol.sql import create_sql_datasource
from tol.sql.session import create_session_factory

import tolqc.assembly_models
import tolqc.folder_models
import tolqc.sample_data_models
import tolqc.system_models
from tolqc.auth import create_auth_ctx_setter
from tolqc.database import build_database_factory, flask_session, logbase_hook_params
from tolqc.json import JSONDateTimeProvider
from tolqc.loaders import loaders_blueprint
from tolqc.model import Base
from tolqc.reports import reports_blueprint
from tolqc.system_models import Token


def models_list():
    """
    The call to `configure_mappers()` is triggered lazily by SQLAlchemy when
    the first instance of a model is created.  Since we dynamically create an
    `EditBase` class for each `LogBase` subclass, we need to call
    `configure_mappers()` here to trigger creation of the `EditBase`
    subclasses and generate the full list of models.
    """
    configure_mappers()

    # Exclude Token class from API
    return tuple(x for m in Base.registry.mappers if (x := m.class_) != Token)


def application(session_factory=None):
    """
    The `session_factory` and `database_factory` arguments are used during
    testing.
    """

    app = Flask(__name__)
    app.json = JSONDateTimeProvider(app)
    if os.getenv('ECHO_SQL'):
        logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
    if os.getenv('TOLQC_DEBUG'):
        logging.getLogger().setLevel(logging.DEBUG)

    api_path = os.getenv('TOLQC_API_PATH', os.getenv('API_PATH', '/api/v1'))
    logging.debug(f'{api_path = }')

    db_uri = os.getenv('DB_URI')
    if not session_factory:
        session_factory = create_session_factory(db_uri)

    auth_ctx_setter = create_auth_ctx_setter(session_factory)

    @app.before_request
    def set_auth_ctx() -> None:
        token = request.headers.get('token')
        if token is not None:
            auth_ctx_setter(token)

    @app.teardown_request
    def remove_before_flush_hook(t_dwn):
        if ssn := flask_session():
            logging.debug(f'Tearing down {ssn = }')
            # Session.close() must be called to avoid SELECT statements
            # accumulating on server with 'idle in transaction' state.
            # (Alternative is to use `Session` as a context manager.)
            ssn.close()
        if hook_params := logbase_hook_params():
            logging.debug(f'Removing {hook_params = }')
            remove(*hook_params)

    models = models_list()
    database_factory = build_database_factory(session_factory, models)

    # Tol QC endpoints
    tolqc_ds = create_sql_datasource(
        models=models,
        db_uri=db_uri,
        behind_api=True,
        database_factory=database_factory,
    )

    #  *** Ugly private attribute access ***
    session_factory = tolqc_ds._SqlDataSource__db._DefaultDatabase__session_factory

    # Data endpoints
    blueprint_data_tolqc = data_blueprint(
        tolqc_ds,
        auth_inspector=basic_auth_inspector('registered'),
    )
    app.register_blueprint(
        blueprint_data_tolqc,
        name='tolqc',
        url_prefix=api_path + '/data',
    )
    core_data_object(tolqc_ds)

    # Reports
    blueprint_reports = reports_blueprint(
        session_factory,
        url_prefix=api_path + '/report',
    )
    app.register_blueprint(blueprint_reports)

    # Data loaders
    blueprint_loaders = loaders_blueprint(
        session_factory,
        url_prefix=api_path + '/loader',
    )
    app.register_blueprint(blueprint_loaders)

    # System endpoints
    blueprint_system = system_blueprint(tolqc_ds)
    app.register_blueprint(
        blueprint_system,
        url_prefix=api_path + '/system',
    )

    return app
