# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.base import BaseTestCase


class TestEnumMethodsByName(BaseTestCase):
    def test_I_get_by_name_matches_by_id_200(self):
        self.add_I(id=348598, name='testing')
        # get by id
        response_by_id = self.client.open(
            '/api/v1/I/348598',
            method='GET'
        )
        self.assert200(
            response_by_id,
            f'Response body is : {response_by_id.data.decode("utf-8")}'
        )
        # assert that the response is correct
        self.assertEqual(
            response_by_id.json,
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
                                'related': '/I/348598/J'
                            }
                        }
                    }
                }
            }
        )
        # get by name
        response_by_name = self.client.open(
            '/api/v1/I/name/testing',
            method='GET'
        )
        self.assert200(
            response_by_name,
            f'Response body is : {response_by_name.data.decode("utf-8")}'
        )
        # assert that the two are equal
        self.assertEqual(response_by_id.json, response_by_name.json)

    def test_I_get_by_bad_name_404(self):
        # add an irrelevant I
        self.add_I(id=348523, name='nice')
        # get a non-existent name
        response = self.client.open(
            '/api/v1/I/name/not_nice',
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
            '/api/v1/I/name/happy',
            method='PATCH',
            json={
                'data': {
                    'type': 'I',
                    'id': '1337',
                    'attributes': {
                        'description': 'This is a hacker.'
                    }
                }
            },
            headers=self._get_api_key_1()
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
            '/api/v1/I/name/happy',
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
                                'related': '/I/4989/J'
                            }
                        }
                    }
                }
            }
        )
        # assert that no new entry has been created
        response = self.client.open(
            '/api/v1/I/1337',
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
            '/api/v1/I/name/nicely',
            method='PATCH',
            json={
                'data': {
                    'type': 'I',
                    'attributes': {
                        'name': 'new'
                    }
                }
            },
            headers=self._get_api_key_1()
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
                                'related': '/I/1480/J'
                            }
                        }
                    }
                }
            }
        )

    def test_delete_by_name_I(self):
        self.add_I(id=34989, name='day', description='quaint')

        # delete the instance by name
        response_by_name = self.client.open(
            '/api/v1/I/name/day',
            method='DELETE',
            headers=self._get_api_key_1()
        )
        self.assert_status(response_by_name, 204)

        # confirm that it is no longer in the db, by name or id
        response_by_name = self.client.open(
            '/api/v1/I/name/day',
            method='GET'
        )
        self.assert404(
            response_by_name,
            f'Response body is : {response_by_name.data.decode("utf-8")}'
        )
        response_by_id = self.client.open(
            '/api/v1/I/34989',
            method='GET'
        )
        self.assert404(
            response_by_id,
            f'Response body is : {response_by_id.data.decode("utf-8")}'
        )

    def test_relation_list_get_matches_by_name_and_id(self):
        # add two I's
        self.add_I(id=4989, name='happy')
        self.add_I(id=304930, name='go_lucky')
        # add two dependent J's on the first I
        self.add_J(id=2099, i_id=4989)
        self.add_J(id=9890, i_id=4989)
        # add one on the second I
        self.add_J(id=23989, i_id=304930)

        # relation list get by name
        response_by_name = self.client.open(
            '/api/v1/I/name/happy/J',
            method='GET'
        )
        self.assert200(response_by_name)
        # assert that the response is correct
        self.assertEqual(
            response_by_name.json,
            {
                'data': [
                    {
                        'type': 'J',
                        'id': '2099',
                        'relationships': {
                            'I': {
                                'data': {
                                    'id': '4989',
                                    'type': 'I'
                                },
                                'links': {
                                    'related': '/I/4989'
                                }
                            }
                        }
                    },
                    {
                        'type': 'J',
                        'id': '9890',
                        'relationships': {
                            'I': {
                                'data': {
                                    'id': '4989',
                                    'type': 'I'
                                },
                                'links': {
                                    'related': '/I/4989'
                                }
                            }
                        }
                    }
                ]
            }
        )

        # relation list get by id
        response_by_id = self.client.open(
            '/api/v1/I/4989/J',
            method='GET'
        )
        self.assert200(response_by_id)
        # assert that it's equal to the other response
        self.assertEqual(response_by_name.json, response_by_id.json)
