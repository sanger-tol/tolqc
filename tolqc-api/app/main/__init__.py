#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import os
import connexion
from flask_marshmallow import Marshmallow

from main import encoder
from main.model import db

marshmallow = None

def application():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Tree of Life ToLID API'},
                pythonic_params=True)
    app.app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_URI']
    app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app.app)

    # get rid of this global variable somehow, later
    global marshmallow
    marshmallow = Marshmallow(app.app)

    return app
