# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import logging
import os

from flask import Flask, request

from sqlalchemy.event import remove
from sqlalchemy.exc import DBAPIError
from sqlalchemy.orm import configure_mappers

from tol.api_base import data_blueprint, system_blueprint
from tol.api_base.auth import basic_auth_inspector
from tol.board import board_blueprint
from tol.core import core_data_object
from tol.sql import Model, create_sql_datasource
from tol.sql.auth import db_auth_blueprint
from tol.sql.board import create_board_models
from tol.sql.session import create_session_factory

# from tolqc.auth import create_auth_ctx_setter
from tolqc.database import build_database_factory, flask_session, logbase_hook_params
from tolqc.json import JSONDateTimeProvider
from tolqc.loaders import loaders_blueprint
from tolqc.reports import reports_blueprint
from tolqc.schema import models_list, Base, system_models

from .auth import create_auth_inspector

from werkzeug.exceptions import BadRequest

def __get_board_models(
    base_model: Model
) -> tuple[list[Model], Model]:
    board_models = create_board_models(base_model)

    return list(board_models), board_models._user_mixin


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



    @app.teardown_request
    def remove_before_flush_hook(*_):
        if ssn := flask_session():
            logging.debug(f'Tearing down {ssn = }')

            # Ensure session cannot be reused after close()
            ssn.close_resets_only = False

            # Session.close() must be called to avoid SELECT statements
            # accumulating on server with 'idle in transaction' state.
            # (Alternative is to use `Session` as a context manager.)
            ssn.close()
        if hook_params := logbase_hook_params():
            logging.debug(f'Removing {hook_params = }')
            remove(*hook_params)


    board_models, _board_user_mixin = __get_board_models(Base)

    user_mixin = type(
        '',
        (system_models.UserMixin, _board_user_mixin),
        {}
    )

    # auth
    auth_bp = db_auth_blueprint(
        Base,
        os.environ['DB_URI'],
        url_prefix=os.environ['API_PATH'] + '/auth',
        oidc_id_target="email",
        user_mixin_class=user_mixin
    )

    app.register_blueprint(auth_bp)
    auth_bp.register_authenticator(app)

    excluded_models = {x for x in auth_bp.models if x != auth_bp.models.user_class}

    models = models_list(excluded_models)

    # models = [
    #     *models,
    #     *board_models,
    #     auth_bp.models.user_class
    # ]



    # session_factory is now a wrapped factory which returns the same Session
    # instance during each Flask request.
    database_factory, session_factory = build_database_factory(session_factory, models)

    # Tol QC endpoints
    tolqc_ds = create_sql_datasource(
        models=models,
        db_uri=db_uri,
        behind_api=True,
        database_factory=database_factory,
    )

    # Data endpoints
    blueprint_data_tolqc = data_blueprint(
        tolqc_ds,
        auth_inspector=create_auth_inspector(),
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
        models,
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

    # dashboards
    boards_bp = board_blueprint(tolqc_ds)
    app.register_blueprint(
        boards_bp,
        name='custom_boards',
        url_prefix=os.environ['API_PATH'] + '/boards'
    )
    blueprint_board_data = data_blueprint(tolqc_ds)
    app.register_blueprint(
        blueprint_board_data,
        name='boards',
        url_prefix=os.getenv('API_PATH') + '/boards'
    )

    @app.errorhandler(BadRequest)
    def handle_bad_request(exptn):
        return propagate_data_source_error(exptn, 400)

    @app.errorhandler(DBAPIError)
    def handle_db_api_error(exptn):
        return propagate_data_source_error(exptn, 500)

    return app


def propagate_data_source_error(exptn: Exception, code: int):
    """Return an error which will be interpreted as a DataSourceError by the client"""
    error_class = exptn.__class__.__name__
    logging.warning(f'{error_class} - {exptn}')
    return {
        'errors': [
            {
                'title': error_class,
                'detail': str(exptn),
            }
        ]
    }, code
