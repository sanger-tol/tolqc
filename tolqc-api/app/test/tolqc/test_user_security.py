# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from datetime import datetime
from main.model import TolqcData
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
                'roles': {
                    'links': {
                        'related': '/user/100/roles'
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
        # from creation_log_base
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
            '/api/v1/data',
            method='POST',
            json={
                'data': {
                    'type': 'data',
                    'attributes': {
                        'reads': 'aquatic reeds',
                        'bases': '0x1337',
                        'avg_read_len': 1.01,
                        'read_len_n50': 9.97
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

        # try to modify creation details of existing data instance
        # add the instance
        data_instance = TolqcData()
        data_instance.id = 9090
        data_instance.reads = 'test'
        data_instance.bases = 'another test'
        data_instance.avg_read_len = 4.56
        data_instance.read_len_n50 = 2387.3
        data_instance.created_by = 101
        data_instance.save()

        # try to modify its creator
        response = self.client.open(
            '/api/v1/data/9090',
            method='PATCH',
            json={
                'data': {
                    'type': 'data',
                    'attributes': {
                        'reads': 'aquatic reeds'
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
        # from creation_log_base
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
            '/api/v1/data',
            method='POST',
            json={
                'data': {
                    'type': 'data',
                    'attributes': {
                        'reads': 'Reed Richaads',
                        'bases': 'basement',
                        'avg_read_len': 2389.8,
                        'read_len_n50': 4598.97,
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
        data_instance = TolqcData()
        data_instance.id = 8609
        data_instance.reads = 'cogito ergo sum'
        data_instance.bases = 'based on what?'
        data_instance.avg_read_len = 4.56
        data_instance.read_len_n50 = 2387.3
        data_instance.created_by = 101
        data_instance.save()

        # try to modify its creator
        response = self.client.open(
            '/api/v1/data/8609',
            method='PATCH',
            json={
                'data': {
                    'type': 'data',
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
