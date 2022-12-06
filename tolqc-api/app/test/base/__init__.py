# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.test_case import TestCase

from main import application


class TolqcTestCase(TestCase):
    def create_app(self):
        return application()
