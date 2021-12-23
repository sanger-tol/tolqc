# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main import application
from main.model import db, TolqcUser, TolqcRole

from test.test_case import TestCase

class TolqcTestCase(TestCase):
    def create_app(self):
        return application()