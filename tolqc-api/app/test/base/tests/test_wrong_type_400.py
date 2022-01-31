# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.base import BaseTestCase


class TestWrongType400(BaseTestCase):
    def test_post_D_with_invalid_type_400(self):
        response = self.client.open(
            '/api/v1/D',
            method='POST',
            json={
                'data': {
                    'type': 'invalid_type',
                    'attributes': {
                        'non_nullable_column': 'test'
                    }
                }
            },
            headers=self._get_api_key_1()
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
