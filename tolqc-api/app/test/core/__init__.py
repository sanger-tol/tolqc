# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import os

from flask_testing import TestCase
from flask import Flask, Blueprint
from flask_restx import Api

from main import encoder
from main.model import db

from test.core.models import ModelRelationshipA, \
                             ModelRelationshipB, \
                             ModelWithNullableColumn, \
                             ModelWithNonNullableColumn
from test.core.resources import b_namespace, \
                                c_namespace, \
                                d_namespace


def _setup_api(blueprint):
    api = Api(
        blueprint,
        doc='/ui',
        title="Tree of Life Quality Control"
    )
    api.add_namespace(b_namespace)
    api.add_namespace(c_namespace)
    api.add_namespace(d_namespace)


class BaseTestCase(TestCase):
    def setUp(self):
        self.maxDiff = None
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.query(ModelRelationshipB).delete()
        db.session.query(ModelRelationshipA).delete()
        db.session.query(ModelWithNullableColumn).delete()
        db.session.query(ModelWithNonNullableColumn).delete()
        db.session.commit()

    def create_app(self):
        app = Flask(__name__)
        blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
        _setup_api(blueprint)
        app.register_blueprint(blueprint)
        app.json_encoder = encoder.JSONEncoder
        db_uri = f"postgresql://{os.environ['POSTGRES_USER']}:" \
                 f"{os.environ['POSTGRES_PASSWORD']}@tolqc-db-core-test/core-test"
        app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(app)
        return app

    def add_A(self, **kwargs):
        a_model = ModelRelationshipA(**kwargs)
        a_model.save()

    def add_B(self, **kwargs):
        b_model = ModelRelationshipB(**kwargs)
        b_model.save()

    def add_C(self, **kwargs):
        c_model = ModelWithNullableColumn(**kwargs)
        c_model.save()

    def add_D(self, **kwargs):
        d_model = ModelWithNonNullableColumn(**kwargs)
        d_model.save()
    
    def to_json_api(self, id, type, json):
        return {
            'data': {
                'type': type,
                'id': id,
                'attributes': json
            }
        }
