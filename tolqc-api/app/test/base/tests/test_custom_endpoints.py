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
            json=data
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        self.assertEqual(
            response.json,
            data
        )
