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


def models_list():
    return [
        *tolqc.assembly_models.models_list(),
        *tolqc.sample_data_models.models_list(),
    ]


def application():
    app = Flask(__name__)

    # Tol QC endpoints
    tolqc_ds = create_sql_datasource(
        models=models_list(),
        db_uri=os.getenv('DB_URI'),
    )
    authenticator = quick_and_dirty_auth(os.getenv('API_TOKEN'))

    # Data endpoints
    blueprint_data_tolqc = data_blueprint(
        tolqc_ds, authenticator=authenticator
    )
    app.register_blueprint(
        blueprint_data_tolqc,
        name='tolqc',
        url_prefix=os.getenv('API_PATH'),
    )
    core_data_object(tolqc_ds)

    # System endpoints
    blueprint_system = system_blueprint(sql_datasource)
    app.register_blueprint(
        blueprint_system,
        url_prefix=os.getenv('API_PATH') + '/system',
    )

    return app
