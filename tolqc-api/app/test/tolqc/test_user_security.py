# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from datetime import datetime
from main.model import TolqcAssemblyComponent
from test.tolqc import TolqcTestCase


class TestUserSecurity(TolqcTestCase):
    def test_no_credential_disclosure_get_users(self):
        expected_user = {
            "type": "user",
            "attributes": {
                "name": "test_user_admin",
                "email": "test_user_admin@sanger.ac.uk",
                "organisation": "Sanger Institute"
            },
            "id": "100",
            'relationships': {
                'role': {
                    'links': {
                        'related': '/user/100/role'
                    }
                }
            }
        }

        # assert no credential disclosure in list get
        response = self.client.open(
            '/api/v1/user?filter=[name=="test_user_admin"]',
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
            '/api/v1/user/100',
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
        filtering against api_key value on list get users, is not
        possible."""
        response = self.client.open(
            f'/api/v1/user?filter=[api_key=="{self.api_key_1}"]',
            method='GET'
        )
        self.assert400(response)

    def test_no_overwrite_creator_in_request(self):
        """Ensures that an authenticated user can not defraud the
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
            '/api/v1/assembly_component',
            method='POST',
            json={
                'data': {
                    'type': 'assembly_component',
                    'attributes': {
                        'name': 'component_no_1',
                        'description': 'this is a description'
                    },
                    'relationships': {
                        'creator': {
                            'data': {
                                'type': 'user',
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
        assembly_component_instance = TolqcAssemblyComponent()
        assembly_component_instance.id = 4321
        assembly_component_instance.name = 'test'
        assembly_component_instance.description = 'another test'
        assembly_component_instance.created_by = 101
        assembly_component_instance.last_modified_by = 101
        assembly_component_instance.save_create(user_id=101)

        # try to modify its creator
        response = self.client.open(
            '/api/v1/assembly_component/4321',
            method='PATCH',
            json={
                'data': {
                    'type': 'assembly_component',
                    'attributes': {
                        'description': 'this desc has now changed'
                    },
                    'relationships': {
                        'creator': {
                            'data': {
                                'type': 'user',
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
        """Ensures that an authenticated user can not defraud the
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
            '/api/v1/assembly_component',
            method='POST',
            json={
                'data': {
                    'type': 'assembly_component',
                    'attributes': {
                        'name': 'component_no_1',
                        'description': 'this is a description',
                        'created_at': str(datetime.now())
                    },
                    'relationships': {
                        'creator': {
                            'data': {
                                'type': 'user',
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

        # try to modify created_at datetime of existing data instance
        # add the instance
        assembly_component_instance = TolqcAssemblyComponent()
        assembly_component_instance.id = 43
        assembly_component_instance.name = 'test'
        assembly_component_instance.description = 'another test'
        assembly_component_instance.created_by = 101
        assembly_component_instance.last_modified_by = 101
        assembly_component_instance.save_create(user_id=101)

        # try to modify its creator
        response = self.client.open(
            '/api/v1/assembly_component/43',
            method='PATCH',
            json={
                'data': {
                    'type': 'assembly_component',
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
