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
                        'last_modified_at': created_at,
                        'history': []
                    },
                    'relationships': {
                        'creator': {
                            'data': {
                                'id': '100',
                                'type': 'user'
                            },
                            'links': {
                                'related': '/user/100'
                            }
                        },
                        'last_modifier': {
                            'data': {
                                'id': '100',
                                'type': 'user'
                            },
                            'links': {
                                'related': '/user/100'
                            }
                        }
                    }
                }
            }
        )

        # patch this to new state
        response = self.client.open(
            f'/api/v1/H/{instance_id}',
            method='PATCH',
            json={
                "data": {
                    "type": 'H',
                    "attributes": {
                        'string_column': 'how are you?'
                    }
                }
            },
            headers=self._get_api_key_2()
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        # pull out unpredictable elements
        last_modified_at_1 = response.json['data']['attributes']['last_modified_at']
        # assert that history has one entry, and is correct
        self.assertEqual(
            response.json,
            {
                'data': {
                    'type': 'H',
                    'id': instance_id,
                    'attributes': {
                        'string_column': 'how are you?',
                        'created_at': created_at,
                        'last_modified_at': last_modified_at_1,
                        'history': [{
                            'string_column': 'hello there',
                            'entered_at': created_at,
                            'entered_by': '100'
                        }]
                    },
                    'relationships': {
                        'creator': {
                            'data': {
                                'id': '100',
                                'type': 'user'
                            },
                            'links': {
                                'related': '/user/100'
                            }
                        },
                        'last_modifier': {
                            'data': {
                                'id': '101',
                                'type': 'user'
                            },
                            'links': {
                                'related': '/user/101'
                            }
                        }
                    }
                }
            }
        )

        # patch this to another new state
        response = self.client.open(
            f'/api/v1/H/{instance_id}',
            method='PATCH',
            json={
                "data": {
                    "type": 'H',
                    "attributes": {
                        'string_column': None
                    }
                }
            },
            headers=self._get_api_key_1()
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        # pull out unpredictable elements
        last_modified_at_2 = response.json['data']['attributes']['last_modified_at']
        # assert that history has one entry, and is correct
        self.assertEqual(
            response.json,
            {
                'data': {
                    'type': 'H',
                    'id': instance_id,
                    'attributes': {
                        'string_column': None,
                        'created_at': created_at,
                        'last_modified_at': last_modified_at_2,
                        'history': [
                            {
                                'string_column': 'hello there',
                                'entered_at': created_at,
                                'entered_by': '100'
                            },
                            {
                                'string_column': 'how are you?',
                                'entered_at': last_modified_at_1,
                                'entered_by': '101'
                            }
                        ]
                    },
                    'relationships': {
                        'creator': {
                            'data': {
                                'id': '100',
                                'type': 'user'
                            },
                            'links': {
                                'related': '/user/100'
                            }
                        },
                        'last_modifier': {
                            'data': {
                                'id': '100',
                                'type': 'user'
                            },
                            'links': {
                                'related': '/user/100'
                            }
                        }
                    }
                }
            }
        )

    def test_no_history_change_on_failed_patch(self):
        # post in the instance
        response = self.client.open(
            '/api/v1/H',
            method='POST',
            json={
                "data": {
                    "type": 'H',
                    "attributes": {
                        'string_column': 'a worthy adversary'
                    }
                }
            },
            headers=self._get_api_key_1()
        )
        self.assert201(response)

        # get the non-predictable data
        instance_id = response.json['data']['id']
        created_at = response.json['data']['attributes']['created_at']

        # delibrately fail a patch request by specifying a bad attribute
        response = self.client.open(
            f'/api/v1/H/{instance_id}',
            method='PATCH',
            json={
                "data": {
                    "type": 'H',
                    "attributes": {
                        'bad_column': 'this will break'
                    }
                }
            },
            headers=self._get_api_key_1()
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

        # get the instance
        response = self.client.open(
            f'/api/v1/H/{instance_id}',
            method='GET'
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

        # assert no history has yet been created
        self.assertEqual(
            response.json,
            {
                'data': {
                    'type': 'H',
                    'id': instance_id,
                    'attributes': {
                        'string_column': 'a worthy adversary',
                        'created_at': created_at,
                        'last_modified_at': created_at,
                        'history': []
                    },
                    'relationships': {
                        'creator': {
                            'data': {
                                'id': '100',
                                'type': 'user'
                            },
                            'links': {
                                'related': '/user/100'
                            }
                        },
                        'last_modifier': {
                            'data': {
                                'id': '100',
                                'type': 'user'
                            },
                            'links': {
                                'related': '/user/100'
                            }
                        }
                    }
                }
            }
        )
