# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.base import BaseTestCase


class TestCustomEndpoints(BaseTestCase):
    def test_custom_endpoint_simple_list_get_200(self):
        response = self.client.open(
            '/api/v1/H/42',
            method='GET'
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        self.assertEqual(
            response.json,
            {
                'data': 42
            }
        )

    def test_custom_endpoint_parrot_post_with_auth_200(self):
        data = {
            'data': {
                'name': 'parrots are fun',
                'array': [
                    24,
                    4587,
                    42
                ]
            }
        }
        response = self.client.open(
            '/api/v1/enum/I/parrot',
            method='POST',
            json=data,
            headers=self._get_api_key_1_headers()
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        self.assertEqual(
            response.json,
            data
        )

    def test_custom_endpoint_parrot_post_with_no_auth_401(self):
        data = {
            'data': {
                'name': 'parrots need permissions',
                'array': [
                    24,
                    4587,
                    42
                ]
            }
        }
        # POST with no auth headers
        response = self.client.open(
            '/api/v1/enum/I/parrot',
            method='POST',
            json=data
        )
        self.assert401(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
