# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.core import BaseTestCase


class TestBadForeignKey400(BaseTestCase):
    def test_post_B_with_bad_foreign_key_error(self):
        self.add_A(id=20)

        response = self.client.open(
            '/api/v1/B',
            method='POST',
            json=[{
                "a_id": 9999
            }]
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        errors = response.json['meta']['errors']
        self.assertEqual(len(errors), 1)
        self.assertNotEqual(errors[0], None)

    def test_put_B_with_bad_foreign_key_400(self):
        self.add_A(id=50)
        self.add_B(id=26, a_id=50)

        response = self.client.open(
            '/api/v1/B/26',
            method='PUT',
            json={
                'a_id': 99999
            }
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
