# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.base import BaseTestCase


class TestHistoryColumnLogBase(BaseTestCase):
    def test_compose_post_patch_H(self):
        # post in the first instance
        response = self.client.open(
            '/api/v1/H',
            method='POST',
            json={
                "data": {
                    "type": 'H',
                    "attributes": {
                        'string_column': 'hello there'
                    }
                }
            },
            headers=self._get_api_key_1()
        )
        self.assert201(response)
        # pull out unpredictable elements
        instance_id = response.json['data']['id']
        created_at = response.json['data']['attributes']['created_at']
        # assert that the history is empty
        self.assertEqual(
            response.json,
            {
                'data': {
                    'type': 'H',
                    'id': instance_id,
                    'attributes': {
                        'string_column': 'hello there',
                        'created_at': created_at,
                        'last_modified_at': None,
                        'history': []
                    },
                    'relationships': {
                        'creator': {
                            'data': {
                                'id': '100',
                                'type': 'users'
                            },
                            'links': {
                                'related': '/users/100'
                            }
                        },
                        'last_modifier': {
                            'data': None
                        }
                    }
                }
            }
        )
