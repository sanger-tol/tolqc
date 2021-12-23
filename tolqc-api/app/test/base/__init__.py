# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import os

from flask import Flask, Blueprint
from flask_restx import Api

from main import encoder
from main.model import db

from test.test_case import TestCase
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
    def create_app(self):
        app = Flask(__name__)
        blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
        _setup_api(blueprint)
        app.register_blueprint(blueprint)
        app.json_encoder = encoder.JSONEncoder
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_URI']
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

