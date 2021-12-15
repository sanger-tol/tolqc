# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.core import BaseTestCase


class TestPut200(BaseTestCase):
    def test_put_B_200(self):
        # first, second, and third A
        self.add_A(
            id=1
        )
        self.add_A(
            id=101
        )
        self.add_A(
            id=10101
        )
        self.add_B(
            id=290,
            a_id=1
        )

        expected = {
            'a_id': 101
        }
        response = self.client.open(
            '/api/v1/B/290',
            method='PUT',
            json={
                'a_id': 101
            }
        )
        self.assert200(response)
        self.assertEqual(response.json['data']['attributes'], expected)

        expected = {
            'a_id': 10101
        }
        response = self.client.open(
            '/api/v1/B/290',
            method='PUT',
            json={
                'a_id': 10101
            }
        )
        self.assert200(response)
        self.assertEqual(response.json['data']['attributes'], expected)
