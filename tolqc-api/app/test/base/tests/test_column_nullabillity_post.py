# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.base import BaseTestCase


class TestColumnNullabilityPost(BaseTestCase):
    def test_collumn_nullabillity_post_C_no_error(self):
        response = self.client.open(
            '/api/v1/C',
            method='POST',
            json={
                "data": {
                    "type": "C",
                    "attributes": {
                        "other_column": "no matter"
                    }
                }
            },
            headers=self._get_api_key_1()
        )
        self.assert201(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        self.assertEqual(
            response.json,
            {
                "data": {
                    "type": "C",
                    "attributes": {
                        "other_column": "no matter",
                        "nullable_column": None
                    },
                    "id": response.json['data']['id']
                },
            }
        )

    def test_non_nullable_column_omitted_post_D_error(self):
        response = self.client.open(
            '/api/v1/D',
            method='POST',
            json={
                "data": {
                    "type": "D",
                    "attributes": {
                        "other_column": "no matter"
                    }
                }
            },
            headers=self._get_api_key_1()
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
