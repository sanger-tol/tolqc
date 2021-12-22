# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import os

from flask_testing import TestCase
from flask import Flask, Blueprint
from flask_restx import Api

from main import encoder
from main.model import db

from test.base.models import ModelRelationshipA, \
                             ModelRelationshipB, \
                             ModelWithNullableColumn, \
                             ModelWithNonNullableColumn, \
                             ModelRelationshipE, \
                             ModelWithExtField


def _setup_api(blueprint):
    api = Api( # noqa
        blueprint,
        doc='/ui',
        title="Tree of Life Quality Control"
    )
    # add api's here


class BaseTestCase(TestCase):
    def setUp(self):
        self.maxDiff = None
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.rollback()
        db.session.query(ModelRelationshipE).delete()
        db.session.query(ModelRelationshipB).delete()
        db.session.query(ModelRelationshipA).delete()
        db.session.query(ModelWithNullableColumn).delete()
        db.session.query(ModelWithNonNullableColumn).delete()
        db.session.query(ModelWithExtField).delete()
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
        self._add_model_instance(ModelRelationshipA, **kwargs)

    def add_B(self, **kwargs):
        self._add_model_instance(ModelRelationshipB, **kwargs)

    def add_C(self, **kwargs):
        self._add_model_instance(ModelWithNullableColumn, **kwargs)

    def add_D(self, **kwargs):
        self._add_model_instance(ModelWithNonNullableColumn, **kwargs)

    def add_E(self, **kwargs):
        self._add_model_instance(ModelRelationshipE, **kwargs)

    def add_F(self, **kwargs):
        self._add_model_instance(ModelWithExtField, **kwargs)

    def to_json_api(self, id, type, attributes):
        return {
            'data': {
                'type': type,
                'id': id,
                'attributes': attributes
            }
        }
