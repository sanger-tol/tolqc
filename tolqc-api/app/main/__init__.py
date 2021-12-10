#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask import Flask

from main import encoder
from main.config import set_config
from main.model import db
from main.route import init_blueprint


def application():
    app = Flask(__name__)
    set_config(app)
    blueprint = init_blueprint(app)
    app.register_blueprint(blueprint)
    app.json_encoder = encoder.JSONEncoder
    db.init_app(app)
    return app
