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
            headers=self._get_api_key_1()
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
