# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from . import BaseTestCase


class FakeTest(BaseTestCase):
    def test(self):
        self.assertEqual(True, True) # noqa