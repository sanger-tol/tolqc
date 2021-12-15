# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.core import BaseTestCase


class TestColumnNullabilityPost(BaseTestCase):
    def test_nullable_column_omitted_post_C_no_error(self):
        response = self.client.open(
            '/api/v1/C',
            method='POST',
            json=[{
                "other_column": "no matter"
            }]
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        errors = response.json['meta']['errors']
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0], None)

    def test_non_nullable_column_omitted_post_D_error(self):
        response = self.client.open(
            '/api/v1/D',
            method='POST',
            json=[{
                "other_column": "no matter"
            }]
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        errors = response.json['meta']['errors']
        self.assertEqual(len(errors), 1)
        self.assertNotEqual(errors[0], None)
