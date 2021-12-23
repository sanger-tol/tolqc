# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import os

from flask_testing import TestCase
from flask import Flask, Blueprint
from flask_restx import Api

from main import encoder
from main.model import db

from test.base.models import A_ModelRelationship, \
                             B_ModelRelationship, \
                             C_ModelWithNullableColumn, \
                             D_ModelWithNonNullableColumn, \
                             E_ModelRelationship, \
                             F_ModelWithExtField
from test.base.resources import api_B, api_C, api_D, api_F


def _setup_api(blueprint):
    api = Api(
        blueprint,
        doc='/ui',
        title="Tree of Life Quality Control"
    )
    api.add_namespace(api_B, '/B')
    api.add_namespace(api_C, '/C')
    api.add_namespace(api_D, '/D')
    api.add_namespace(api_F, '/F')


class BaseTestCase(TestCase):
    def setUp(self):
        self.maxDiff = None
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.rollback()
        db.session.query(E_ModelRelationship).delete()
        db.session.query(B_ModelRelationship).delete()
        db.session.query(A_ModelRelationship).delete()
        db.session.query(C_ModelWithNullableColumn).delete()
        db.session.query(D_ModelWithNonNullableColumn).delete()
        db.session.query(F_ModelWithExtField).delete()
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

    def _add_model_instance(self, model, **kwargs):
        model(**kwargs).save()

    def add_A(self, **kwargs):
        self._add_model_instance(A_ModelRelationship, **kwargs)

    def add_B(self, **kwargs):
        self._add_model_instance(B_ModelRelationship, **kwargs)

    def add_C(self, **kwargs):
        self._add_model_instance(C_ModelWithNullableColumn, **kwargs)

    def add_D(self, **kwargs):
        self._add_model_instance(D_ModelWithNonNullableColumn, **kwargs)

    def add_E(self, **kwargs):
        self._add_model_instance(E_ModelRelationship, **kwargs)

    def add_F(self, **kwargs):
        self._add_model_instance(F_ModelWithExtField, **kwargs)

    def to_json_api(self, id, type, attributes):
        return {
            'data': {
                'type': type,
                'id': id,
                'attributes': attributes
            }
        }
