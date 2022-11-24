# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask_testing import TestCase as FlaskTestCase
from tol.api_base.model import db


class TestCase(FlaskTestCase):

    def setUp(self):
        self.maxDiff = None
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.rollback()

    def assert201(self, response, *args):
        self.assertEqual(response.status_code, 201)
