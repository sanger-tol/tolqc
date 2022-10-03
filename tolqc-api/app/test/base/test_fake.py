# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.base import TolqcTestCase


class TestFake(TolqcTestCase):
    def test_fake(self):
        self.assertEqual(True, True)
