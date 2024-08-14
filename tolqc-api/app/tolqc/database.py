# SPDX-FileCopyrightText: 2024 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import logging
from typing import Callable

import flask

from sqlalchemy.event import listen

from tol.api_base2.misc.auth_context import default_ctx_getter
from tol.sql.database import Database, DefaultDatabase

from tolqc.schema.base import update_logbase_closure


__ssn_key = 'TOLQC_FLASK_SESSION'


def build_database_factory(session_factory, models_list) -> (Database, Callable):
    def sesssion_factory_wrapper():
        ssn = flask.g.get(__ssn_key)
        if not ssn:
            ssn = flask.g.setdefault(__ssn_key, build_flask_session(session_factory))
        return ssn

    def db_factory(*_):
        return DefaultDatabase(sesssion_factory_wrapper, models_list)

    return db_factory, sesssion_factory_wrapper


def flask_session():
    return flask.g.get(__ssn_key)


__hook_key = 'TOLQC_HOOK_PARAMS'


def build_flask_session(session_factory):
    ssn = session_factory()
    ssn.close_resets_only = False
    logging.debug(f'Created {ssn = }')

    ctx = default_ctx_getter()
    if ctx.authenticated:
        user_id = ctx.user_id
        logging.debug(f'Adding LogBase updater hook for {user_id = }')
        hook_params = ssn, 'before_flush', update_logbase_closure(user_id)
        flask.g.setdefault(__hook_key, hook_params)
        listen(*hook_params)

    return ssn


def logbase_hook_params():
    return flask.g.get(__hook_key)
