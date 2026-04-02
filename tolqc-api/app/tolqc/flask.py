# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import logging
import os
from datetime import timedelta

from flask import Flask

from flask_cors import CORS

from sqlalchemy.event import remove
from sqlalchemy.exc import DBAPIError

from tol.api_base import (
    action_blueprint,
    data_blueprint,
    system_blueprint
)
from tol.api_base.auth import env_oidc_config
from tol.core import DataSourceUtils
from tol.sources.portaldb import portaldb
from tol.sources.prefect import prefect
from tol.sql.auth.blueprint import DbAuthBlueprint, DbAuthManager
from tol.sql.session import create_session_factory

from tolqc.database import build_database_factory, flask_session, logbase_hook_params
from tolqc.json import JSONDateTimeProvider
from tolqc.loaders import loaders_blueprint
from tolqc.reports import reports_blueprint
from tolqc.schema import auth_models, models_list

from werkzeug.exceptions import BadRequest

def application(session_factory=None):
    """
    The `session_factory` and `database_factory` arguments are used during
    testing.
    """
    models = models_list()

    app = Flask(__name__)
    app.json = JSONDateTimeProvider(app)
    if os.getenv('ECHO_SQL'):
        logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
    if os.getenv('TOLQC_DEBUG'):
        logging.getLogger().setLevel(logging.DEBUG)

    api_path = os.getenv('TOLQC_API_PATH', os.getenv('API_PATH', '/api/v1'))
    api_data_path = os.getenv('TOLQC_API_DATA_PATH', os.getenv('API_DATA_PATH', '/data'))
    logging.debug(f'{api_path = }')
    logging.debug(f'{api_data_path = }')

    CORS(app, resources={r'/api/*': {'origins': '*'}})
    app.config['CORS_HEADERS'] = 'Content-Type'

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

    # auth
    auth_manager = DbAuthManager(
        oidc_config=env_oidc_config(),
        session_factory=session_factory,
        model_tuple=auth_models,
        state_delete_delta=timedelta(hours=1),
        oidc_id_target='email',
        oidc_ext_mapping={},
        authorisation_manager=None,
    )
    auth_bp = DbAuthBlueprint(
        auth_manager,
        api_path + '/auth',
        auth_models,
    )

    app.register_blueprint(auth_bp)
    auth_bp.register_authenticator(app)

    # session_factory is now a wrapped factory which returns the same Session
    # instance during each Flask request.
    database_factory, session_factory = build_database_factory(session_factory, models)

    portaldb_ds = portaldb()
    portaldb_ds.page_size = 500
    instance_name = 'tolqc_internal'
    tolqc_datasource_instance = portaldb_ds.get_one('data_source_instance', instance_name)
    if not tolqc_datasource_instance:
        msg = f"Failed to get data_source_instance = '{instance_name}'"
        raise ValueError(msg)
    tolqc_ds = DataSourceUtils.get_datasource_by_datasource_instance(
        tolqc_datasource_instance,
        models=models,
        db_uri=db_uri,
        behind_api=True,
        database_factory=database_factory,
    )

    # Data endpoints
    blueprint_data_tolqc = data_blueprint(
        tolqc_ds,
        include_all_to_ones=False,
    )
    app.register_blueprint(
        blueprint_data_tolqc,
        name='tolqc',
        url_prefix=api_path + api_data_path,
    )

    # Reports
    blueprint_reports = reports_blueprint(
        session_factory,
        models,
        url_prefix=api_path + '/report',
    )
    app.register_blueprint(blueprint_reports)

    # actions
    pds = prefect(insecure=True)
    actions_bp = action_blueprint(
        tolqc_ds,
        pds,
        role=None
    )
    app.register_blueprint(
        actions_bp,
        url_prefix=api_path + '/local/run-action'
    )
    blueprint_prefect_data = data_blueprint(
        pds
    )
    app.register_blueprint(
        blueprint_prefect_data,
        name='pds',
        url_prefix=api_path + '/prefect'
    )

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
