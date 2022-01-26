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
            '/api/v1/users',
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
        response = self.client.open(
            f'/api/v1/users?filter=[api_key=="{self.api_key}"]',
            method='GET'
        )
        self.assert400(response)
