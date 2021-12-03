# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.core import BaseTestCase


class TestEmptyRequestBody400(BaseTestCase):
    def test_post_B_with_empty_request_body_400(self):
        response = self.client.open(
            '/api/v1/B',
            method='POST',
            json={}
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
    
    def test_post_C_with_empty_request_body_400(self):
        response = self.client.open(
            '/api/v1/C',
            method='POST',
            json={}
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
    
    def test_post_D_with_empty_request_body_400(self):
        response = self.client.open(
            '/api/v1/D',
            method='POST',
            json={}
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

    def test_put_B_with_empty_request_body_400(self):
        self.add_A(id=44)
        self.add_B(id=77, a_id=44)
        response = self.client.open(
            '/api/v1/B/77',
            method='PUT',
            json={}
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

    def test_put_C_with_empty_request_body_400(self):
        self.add_C(id=45)
        response = self.client.open(
            '/api/v1/C/45',
            method='PUT',
            json={}
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

    def test_put_D_with_empty_request_body_400(self):
        self.add_D(id=49, non_nullable_column='this column')
        response = self.client.open(
            '/api/v1/D/49',
            method='PUT',
            json={}
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
