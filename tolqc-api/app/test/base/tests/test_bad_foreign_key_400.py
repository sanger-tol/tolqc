# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.base import BaseTestCase


class TestBadForeignKey400(BaseTestCase):
    def test_post_B_with_bad_foreign_key_error(self):
        self.add_A(id=20)

        response = self.client.open(
            '/api/v1/B',
            method='POST',
            json={
                "data": {
                    "type": 'B',
                    "attributes": {},
                    "relationships": {
                        "A": {
                            "data": {
                                "type": 'A',
                                "id": 9999
                            }
                        }
                    }
                }
            },
            headers=self._get_api_key_1_headers()
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
