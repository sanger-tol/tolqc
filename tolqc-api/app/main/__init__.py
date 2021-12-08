#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import os
import logging
from flask import Flask

from main import encoder
from main.model import db
from main.route import blueprint


def application():
    app = Flask(__name__)
    app.register_blueprint(blueprint)
    app.json_encoder = encoder.JSONEncoder
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app
