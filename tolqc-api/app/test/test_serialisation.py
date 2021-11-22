# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model.tolqc_centre import TolqcCentre
from test import BaseTestCase


class TestSerialisation(BaseTestCase):
    def test_tolqc_centre(self):
        test_tolqc_centre = TolqcCentre()
        test_tolqc_centre.name = "A good name"
        test_tolqc_centre.hierarchy_name = "A brilliant hierarchy name"
        test_tolqc_centre.centre_id = 101

        expected = dict(
            name = "A good name",
            hierarchy_name = "A brilliant hierarchy name",
            centre_id = 101
        )
        received = test_tolqc_centre.to_dict()

        self.assertEqual(expected, received)
