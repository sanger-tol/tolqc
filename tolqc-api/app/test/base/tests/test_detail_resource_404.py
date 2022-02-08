# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.base import BaseTestCase


class TestDetailResource404(BaseTestCase):
    def test_get_B_404(self):
        response = self.client.open(
            '/api/v1/B/9999',
            method='GET',
        )
        self.assert404(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

    def test_get_C_404(self):
        response = self.client.open(
            '/api/v1/C/9999',
            method='GET',
        )
        self.assert404(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

    def test_get_D_404(self):
        response = self.client.open(
            '/api/v1/D/9999',
            method='GET',
        )
        self.assert404(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

    def test_delete_B_404(self):
        response = self.client.open(
            '/api/v1/B/9999',
            method='DELETE',
            headers=self._get_api_key_1_headers()
        )
        self.assert404(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

    def test_delete_C_404(self):
        response = self.client.open(
            '/api/v1/C/9999',
            method='DELETE',
            headers=self._get_api_key_1_headers()
        )
        self.assert404(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

    def test_delete_D_404(self):
        response = self.client.open(
            '/api/v1/D/9999',
            method='DELETE',
            headers=self._get_api_key_1_headers()
        )
        self.assert404(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

    def test_patch_B_404(self):
        response = self.client.open(
            '/api/v1/B/9999',
            method='PATCH',
            json={
                "data": {
                    "attributes": {
                        "a_id": 0
                    },
                    "type": "B"
                }
            },
            headers=self._get_api_key_1_headers()
        )
        self.assert404(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

    def test_patch_C_404(self):
        response = self.client.open(
            '/api/v1/C/9999',
            method='PATCH',
            json={
                "data": {
                    "type": "C",
                    "attributes": {
                        "nullable_column": 'test_string'
                    }
                }
            },
            headers=self._get_api_key_1_headers()
        )
        self.assert404(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

    def test_patch_D_404(self):
        response = self.client.open(
            '/api/v1/D/9999',
            method='PATCH',
            json={
                "data": {
                    "type": "D",
                    "attributes": {
                        "non_nullable_column": 'ANOTHER TEST STRING'
                    }
                }
            },
            headers=self._get_api_key_1_headers()
        )
        self.assert404(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
