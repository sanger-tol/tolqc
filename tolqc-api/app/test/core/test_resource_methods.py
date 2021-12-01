# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.core import BaseTestCase


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
        )
        self.assert404(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
    
    def test_delete_C_404(self):
        response = self.client.open(
            '/api/v1/C/9999',
            method='DELETE',
        )
        self.assert404(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
    
    def test_delete_D_404(self):
        response = self.client.open(
            '/api/v1/D/9999',
            method='DELETE',
        )
        self.assert404(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
    
    def test_put_B_404(self):
        response = self.client.open(
            '/api/v1/B/9999',
            method='PUT',
            json={
                "a_id": 0
            }
        )
        self.assert404(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

    def test_put_C_404(self):
        response = self.client.open(
            '/api/v1/C/9999',
            method='PUT',
            json={
                "nullable_column": 'test_string'
            }
        )
        self.assert404(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
    
    def test_put_D_404(self):
        response = self.client.open(
            '/api/v1/D/9999',
            method='PUT',
            json={
                "non_nullable_column": 'ANOTHER TEST STRING'
            }
        )
        self.assert404(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
