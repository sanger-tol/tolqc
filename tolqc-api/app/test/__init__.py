# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import logging

import connexion
from flask_testing import TestCase
import os

from main.encoder import JSONEncoder

from main.model import db, TolqcUser, TolqcRole


class BaseTestCase(TestCase):

    api_key = "AnyThingBecAuseThIsIsATEST567890"

    def setUp(self):
        self.maxDiff = None
        db.create_all()
        user1 = TolqcUser(user_id=100,
                          name="test_user_admin",
                          email="test_user_admin@sanger.ac.uk",
                          organisation="Sanger Institute",
                          api_key=self.api_key)
        db.session.add(user1)
        role = TolqcRole(role="admin")
        role.user = user1
        db.session.add(role)
        db.session.commit()

    def tearDown(self):
        db.session.query(TolqcRole).delete()
        db.session.query(TolqcUser).delete()
        db.session.commit()

    def create_app(self):
        logging.getLogger('connexion').setLevel('ERROR')
        logging.getLogger('openapi_spec_validator').setLevel('ERROR')
        app = connexion.App(__name__, specification_dir='../main/swagger/')
        app.app.json_encoder = JSONEncoder
        app.add_api('swagger.yaml', pythonic_params=True)
        app.app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_URI']
        app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(app.app)
        return app.app
