# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.core import BaseTestCase


class TestGetInsertedData(BaseTestCase):
    def test_get_inserted_B(self):
        self.add_A(id=90)
        self.add_B(id=10, a_id=90)

        expected = self.to_json_api(
            10,
            'B',
            {
                "a_id": 90,
            },
        )

        response = self.client.open(
            '/api/v1/B/10',
            method='GET',
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        self.assertEqual(expected, response.json)
