# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.base import BaseTestCase


class TestBadFieldsError(BaseTestCase):
    def test_B_id_in_request_body_post_400(self):
        self.add_A(id=9090)
        response = self.client.open(
            '/api/v1/B',
            method='POST',
            json={
                'data': {
                    'id': 9999,
                    'type': 'B',
                },
                "relationships": {
                    "A": {
                        "data": {
                            "type": 'A',
                            "id": 9090
                        }
                    }
                }
            },
            headers=self._get_api_key()
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
