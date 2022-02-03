# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.base import BaseTestCase


class TestEnumLinkRelationshipByName(BaseTestCase):
    def _assert_enum_validation_error(self, response):
        errors = response.json.get('errors', [])
        first_error = {} if not errors else errors[0]
        error_title = first_error.get('title', None)
        self.assertEqual(
            error_title,
            'Validation Error'
        )

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

    def test_post_J_specify_I_by_id(self):
        self.add_I(id=3021349, name='also')
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
                                'id': '3021349'
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
                                'id': '3021349'
                            },
                            'links': {
                                'related': '/I/3021349'
                            }
                        }
                    }
                }
            }
        )

    def test_specify_both_id_and_name_enum_I_for_J_400(self):
        self.add_I(id=4598, name='fair')
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
                                'id': '4598',
                                'name': 'fair'
                            }
                        }
                    }
                }
            }
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        self._assert_enum_validation_error(response)

    def test_specify_neither_id_nor_name_enum_I_for_J_400(self):
        self.add_I(id=32130, name='based')
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
                                'type': 'I'
                            }
                        }
                    }
                }
            }
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        self._assert_enum_validation_error(response)

    def test_specify_bad_name_enum_I_for_J_400(self):
        self.add_I(id=34857, name='epic')
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
                                'name': 'bad_name'
                            }
                        }
                    }
                }
            }
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        self._assert_enum_validation_error(response)

    def test_name_specification_on_non_enum_B_400(self):
        self.add_A(id=39849)
        response = self.client.open(
            '/api/v1/B',
            method='POST',
            headers=self._get_api_key_1(),
            json={
                'data': {
                    'type': 'B',
                    'relationships': {
                        'A': {
                            'data': {
                                'type': 'A',
                                'name': 'name_not_supported'
                            }
                        }
                    }
                }
            }
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        # assert that it failed for the intended reason
        self.assertEqual(
            response.json,
            {
                'errors':
                [{
                    'detail': 'Must have an `id` field',
                    'source': {
                        'pointer': '/data/relationships/A/data'
                    }
                }]
            }
        )
