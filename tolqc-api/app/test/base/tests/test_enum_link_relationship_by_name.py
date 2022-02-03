# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.base import BaseTestCase


class TestEnumLinkRelationshipByName(BaseTestCase):
    def test_post_J_specify_I_by_name(self):
        self.add_I(id=4857, name='nicely')
        response = self.client.open(
            '/api/v1/J',
            method='POST',
            headers=self._get_api_key_1(),
            json={
                'data': {
                    'type': 'J',
                    'relationships': {
                        'I': {
                            'data': {
                                'type': 'I',
                                'name': 'nicely'
                            }
                        }
                    }
                }
            }
        )
        self.assert201(response)
        
        # get non predictable id
        created_id = response.json['data']['id']

        # assert response json is correct
        self.assertEqual(
            response.json,
            {
                'data': {
                    'type': 'J',
                    'id': created_id,
                    'relationships': {
                        'I': {
                            'data': {
                                'type': 'I',
                                'id': '4857'
                            },
                            'links': {
                                'related': '/I/4857'
                            }
                        }
                    }
                }
            }
        )
