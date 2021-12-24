# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.base import BaseTestCase


class TestEmptyRequestBody(BaseTestCase):
    def test_post_D_with_empty_request_body_400(self):
        response = self.client.open(
            '/api/v1/D',
            method='POST',
            json={},
            headers=self._get_api_key()
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
            headers=self._get_api_key()
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
    #TODO add 200 tests with PATCH
