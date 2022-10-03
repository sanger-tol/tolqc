# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.base import BaseTestCase


class TestEmptyRequestBody(BaseTestCase):
    def test_post_D_with_empty_request_body_400(self):
        response = self.client.open(
            '/api/v1/D',
            method='POST',
            json={},
            headers=self._get_api_key_1_headers()
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

    def test_post_D_with_no_data_400(self):
        response = self.client.open(
            '/api/v1/D',
            method='POST',
            json={
                'data': {
                    'type': 'D',
                    'attributes': {}
                }
            },
            headers=self._get_api_key_1_headers()
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

    def test_patch_C_with_empty_request_body_400(self):
        self.add_C(id=9099)
        response = self.client.open(
            '/api/v1/C/9099',
            method='PATCH',
            json={},
            headers=self._get_api_key_1_headers()
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

    def test_patch_C_with_no_attributes_200(self):
        self.add_C(id=9099)
        response = self.client.open(
            '/api/v1/C/9099',
            method='PATCH',
            json={
                'data': {
                    'type': 'C',
                    'attributes': {}
                }
            },
            headers=self._get_api_key_1_headers()
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
