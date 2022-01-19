# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.base import BaseTestCase


class TestUpdatedCorrectly200(BaseTestCase):
    def test_updated_correctly_B_200(self):
        a_id = 109
        new_a_id = 9090
        b_id = 218
        self.add_A(id=a_id)
        self.add_A(id=new_a_id)
        self.add_B(id=b_id, a_id=a_id)

        response = self.client.open(
            f'/api/v1/B/{b_id}',
            method='PATCH',
            json={
                'data': {
                    'type': 'B',
                    'relationships': {
                        "A": {
                            "data": {
                                "type": 'A',
                                "id": str(new_a_id)
                            }
                        }
                    }
                }
            },
            headers=self._get_api_key()
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

        self.assertEqual(
            response.json,
            {
                'data': {
                    'id': str(b_id),
                    'type': 'B',
                    'relationships': {
                        'A': {
                            'data': {
                                'id': str(new_a_id),
                                'type': 'A'
                            },
                            'links': {
                                'related': f'/A/{new_a_id}'
                            }
                        }
                    }
                }
            }
        )
