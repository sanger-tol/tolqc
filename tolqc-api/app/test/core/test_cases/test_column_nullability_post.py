# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.core import BaseTestCase


class TestColumnNullabilityPost(BaseTestCase):
    def test_nullable_column_omitted_post_C_200(self):
        response = self.client.open(
            '/api/v1/C',
            method='POST',
            json={
                "other_column": "no matter"
            }
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

    def test_non_nullable_column_omitted_post_D_400(self):
        response = self.client.open(
            '/api/v1/D',
            method='POST',
            json={
                "other_column": "no matter"
            }
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
