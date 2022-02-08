# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from datetime import datetime
from main.model import TolqcAssemblyComponent
from test.tolqc import TolqcTestCase


class TestusersSecurity(TolqcTestCase):
    def test_no_credential_disclosure_get_users(self):
        expected_user = {
            "type": "users",
            "attributes": {
                "name": "test_users_admin",
                "email": "test_users_admin@sanger.ac.uk",
                "organisation": "Sanger Institute"
            },
            "id": "100",
            'relationships': {
                'roles': {
                    'links': {
                        'related': '/users/100/roles'
                    }
                }
            }
        }

        # assert no credential disclosure in list get
        response = self.client.open(
            '/api/v1/users?filter=[name=="test_user_admin"]',
            method='GET'
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        self.assertEqual(
            response.json,
            {
                "data": [expected_user]
            }
        )

        # assert no credential disclosure in detail get
        response = self.client.open(
            '/api/v1/users/100',
            method='GET'
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        self.assertEqual(
            response.json,
            {
                "data": expected_user
            }
        )

    def test_no_blind_equal_filter_credential_disclosure(self):
        """Ensures that a word-list attack, in which a hacker
        may guess an api_key from a list of likely candidates by
        filtering against api_key value on list get userss, is not
        possible."""
        response = self.client.open(
            f'/api/v1/users?filter=[api_key=="{self.api_key_1}"]',
            method='GET'
        )
        self.assert400(response)

        # assert that it failed for the correct reason
        self.assertEqual(
            response.json,
            {
                'errors': [{
                    'code': 400,
                    'detail': "The filter key 'api_key' is invalid.",
                    'title': 'Bad Request'
                }]
            }
        )

    def test_no_overwrite_creator_in_request(self):
        """Ensures that an authenticated users can not defraud the
        creator log by specifying another creator in a POST or
        PATCH request"""
        # N.B. this method needs an endpoint with a model inheriting
        # from log_base
        expected_response = {
            'errors': [
                {
                    'detail': 'Unknown field.',
                    'source': {
                        'pointer': "/data/relationships/creator/data"
                    }
                }
            ]
        }

        response = self.client.open(
            '/api/v1/enum/assembly_components',
            method='POST',
            json={
                'data': {
                    'type': 'assembly_components',
                    'attributes': {
                        'name': 'component_no_1',
                        'description': 'this is a description'
                    },
                    'relationships': {
                        'creator': {
                            'data': {
                                'type': 'users',
                                'id': '100'
                            }
                        }
                    }
                }
            },
            headers={
                'Authorization': self.api_key_2
            }
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        # assert 400 code for correct reason
        self.assertEqual(response.json, expected_response)

        # try to modify creation details of existing assembly component instance
        # add the instance
        assembly_components_instance = TolqcAssemblyComponent()
        assembly_components_instance.id = 4321
        assembly_components_instance.name = 'test'
        assembly_components_instance.description = 'another test'
        assembly_components_instance.created_by = 101
        assembly_components_instance.last_modified_by = 101
        assembly_components_instance.save_create(user_id=101)

        # try to modify its creator
        response = self.client.open(
            '/api/v1/enum/assembly_components/test',
            method='PATCH',
            json={
                'data': {
                    'type': 'assembly_components',
                    'attributes': {
                        'description': 'this desc has now changed'
                    },
                    'relationships': {
                        'creator': {
                            'data': {
                                'type': 'users',
                                'id': '100'
                            }
                        }
                    }
                }
            },
            headers={
                'Authorization': self.api_key_2
            }
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        # assert 400 code for correct reason
        self.assertEqual(response.json, expected_response)

    def test_no_overwrite_created_at_in_request(self):
        """Ensures that an authenticated users can not defraud the
        creation datetime log by specifying another value in a POST or
        PATCH request"""
        # N.B. this method needs an endpoint with a model inheriting
        # from log_base
        expected_response = {
            'errors': [
                {
                    'detail': 'Unknown field.',
                    'source': {
                        'pointer': "/data/attributes/created_at"
                    }
                }
            ]
        }
        response = self.client.open(
            '/api/v1/enum/assembly_components',
            method='POST',
            json={
                'data': {
                    'type': 'assembly_components',
                    'attributes': {
                        'name': 'component_no_1',
                        'description': 'this is a description',
                        'created_at': str(datetime.now())
                    }
                }
            },
            headers={
                'Authorization': self.api_key_2
            }
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        # assert 400 code for correct reason
        self.assertEqual(response.json, expected_response)

        # try to modify created_at datetime of existing data instance
        # add the instance
        assembly_components_instance = TolqcAssemblyComponent()
        assembly_components_instance.id = 43
        assembly_components_instance.name = 'test'
        assembly_components_instance.description = 'another test'
        assembly_components_instance.created_by = 101
        assembly_components_instance.last_modified_by = 101
        assembly_components_instance.save_create(user_id=101)

        # try to modify its creator
        response = self.client.open(
            '/api/v1/enum/assembly_components/test',
            method='PATCH',
            json={
                'data': {
                    'type': 'assembly_components',
                    'attributes': {
                        'created_at': str(datetime.now())
                    }
                }
            },
            headers={
                'Authorization': self.api_key_2
            }
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        # assert 400 code for correct reason
        self.assertEqual(response.json, expected_response)
