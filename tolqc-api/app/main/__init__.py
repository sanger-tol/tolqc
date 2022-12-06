#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask import Flask

from main.config import set_config
from main.encoder import JSONEncoder
from main.model import db
from main.route import init_blueprints

from tol.api_base.error.handler import blueprint as error_handler


def application():
    app = Flask(__name__)
    set_config(app, JSONEncoder)
    blueprint = init_blueprints(app)
    app.register_blueprint(blueprint)
    app.register_blueprint(error_handler)
    app.json_encoder = JSONEncoder
    db.init_app(app)
    return app
