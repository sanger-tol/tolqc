#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask import Flask

from main.encoder import JSONEncoder
from main.config import set_config
from main.model import db
from main.route import init_blueprint


def application():
    app = Flask(__name__)
    set_config(app, JSONEncoder)
    blueprint = init_blueprint(app)
    app.register_blueprint(blueprint)
    app.json_encoder = JSONEncoder
    db.init_app(app)
    return app
