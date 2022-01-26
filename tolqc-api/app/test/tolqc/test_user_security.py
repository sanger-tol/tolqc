# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.tolqc import TolqcTestCase


class TestUserSecurity(TolqcTestCase):
    def test_no_credential_disclosure_get_users(self):
        expected_user = {
            "type": "users",
            "attributes": {
                "name": "test_user_admin",
                "email": "test_user_admin@sanger.ac.uk",
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
        filtering against api_key value on list get users, is not
        possible."""
        response = self.client.open(
            f'/api/v1/users?filter=[api_key=="{self.api_key_1}"]',
            method='GET'
        )
        self.assert400(response)

    def test_no_overwrite_creator_in_request(self):
        """Ensures that an authenticated user can not defraud the
        creation log by specifying another creator in a POST or
        PATCH request"""
        # N.B. this method needs an endpoint with a model inheriting
        # from creation_log_base
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
        self.assertEqual(
            response.json,
            {
                'errors': [
                    {
                        'detail': 'Unknown field.',
                        'source': {
                            'pointer': "/data/relationships/creator/data"
                        }
                    }
                ]
            }
        )
