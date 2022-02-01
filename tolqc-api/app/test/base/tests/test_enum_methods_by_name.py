# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.base import BaseTestCase


class TestEnumMethodsByName(BaseTestCase):
    def test_I_get_by_name_matches_by_id_200(self):
        self.add_I(id=348598, name='testing')
        response = self.client.open(
            '/api/v1/I',
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
            headers=self._get_api_key_1()
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
