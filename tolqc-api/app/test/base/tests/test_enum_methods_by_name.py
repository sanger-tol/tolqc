# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.base import BaseTestCase


class TestEnumMethodsByName(BaseTestCase):
    def test_I_get_by_name_200(self):
        self.add_I(id=348598, name='testing')
        # get by name
        response = self.client.open(
            '/api/v1/enum/I/testing',
            method='GET'
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        # assert that the response is correct
        self.assertEqual(
            response.json,
            {
                'data': {
                    'type': 'I',
                    'id': '348598',
                    'attributes': {
                        'name': 'testing',
                        'description': None
                    },
                    'relationships': {
                        'J': {
                            'links': {
                                'related': '/enum/I/testing/J'
                            }
                        }
                    }
                }
            }
        )

    def test_I_get_by_bad_name_404(self):
        # add an irrelevant I
        self.add_I(id=348523, name='nice')
        # get a non-existent name
        response = self.client.open(
            '/api/v1/enum/I/not_nice',
            method='GET'
        )
        self.assert404(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

    def test_no_override_id_by_name_patch_400(self):
        # add an I
        self.add_I(id=4989, name='happy')
        # attempt to patch to a new id
        response = self.client.open(
            '/api/v1/enum/I/happy',
            method='PATCH',
            json={
                'data': {
                    'type': 'I',
                    'id': '1337',
                    'attributes': {
                        'name': 'dinosaur',
                        'description': 'This is a hacker.'
                    }
                }
            },
            headers=self._get_api_key_1_headers()
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        # check it failed for the right reason
        self.assertEqual(
            response.json,
            {
                'errors': [{
                    'detail': 'Unknown field.',
                    'source': {
                        'pointer': '/data/id'
                    }
                }]
            }
        )
        # confirm that no state change occured
        response = self.client.open(
            '/api/v1/enum/I/happy',
            method='GET'
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        self.assertEqual(
            response.json,
            {
                'data': {
                    'id': '4989',
                    'type': 'I',
                    'attributes': {
                        'name': 'happy',
                        'description': None
                    },
                    'relationships': {
                        'J': {
                            'links': {
                                'related': '/enum/I/happy/J'
                            }
                        }
                    }
                }
            }
        )
        # assert that no new entry has been created
        response = self.client.open(
            '/api/v1/enum/I/dinosaur',
            method='GET'
        )
        self.assert404(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

    def test_override_name_by_name_patch_200(self):
        # add an I
        self.add_I(id=1480, name='nicely')
        # attempt to patch to a new id
        response = self.client.open(
            '/api/v1/enum/I/nicely',
            method='PATCH',
            json={
                'data': {
                    'type': 'I',
                    'attributes': {
                        'name': 'new'
                    }
                }
            },
            headers=self._get_api_key_1_headers()
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        # assert that the name is overriden
        self.assertEqual(
            response.json,
            {
                'data': {
                    'type': 'I',
                    'id': '1480',
                    'attributes': {
                        'name': 'new',
                        'description': None
                    },
                    'relationships': {
                        'J': {
                            'links': {
                                'related': '/enum/I/new/J'
                            }
                        }
                    }
                }
            }
        )

    def test_delete_by_name_I(self):
        self.add_I(id=34989, name='day', description='quaint')

        # delete the instance by name
        response = self.client.open(
            '/api/v1/enum/I/day',
            method='DELETE',
            headers=self._get_api_key_1_headers()
        )
        self.assert_status(response, 204)

        # confirm that it is no longer in the db
        response = self.client.open(
            '/api/v1/enum/I/day',
            method='GET'
        )
        self.assert404(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

    def test_equivalent_methods_list_get_I_and_J(self):
        # add the data
        self.add_I(id=878, name='excellent')
        self.add_J(id=909090, I='excellent')
        self.add_J(id=8374483, I='excellent')
        self.add_J(id=987, I='excellent')

        # the expected data (should be identical for both)
        expected_data = {
            'data': [
                {
                    'type': 'J',
                    'id': '987',
                    'attributes': {
                        'I': 'excellent'
                    }
                },
                {
                    'type': 'J',
                    'id': '909090',
                    'attributes': {
                        'I': 'excellent'
                    }
                },
                {
                    'type': 'J',
                    'id': '8374483',
                    'attributes': {
                        'I': 'excellent'
                    }
                },
            ]
        }

        # J-relation list get on I
        first_response = self.client.open(
            '/api/v1/enum/I/excellent/J',
            method='GET'
        )
        self.assert200(
            first_response,
            f'Response body is : {first_response.data.decode("utf-8")}'
        )
        # assert that the data is correct
        self.assertEqual(first_response.json, expected_data)

        # list-get on J, filter by I=excellent
        second_response = self.client.open(
            '/api/v1/J?filter=[I=="excellent"]',
            method='GET'
        )
        self.assert200(
            second_response,
            f'Response body is : {second_response.data.decode("utf-8")}'
        )
        # assert that the data is correct
        self.assertEqual(second_response.json, expected_data)
