# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.core import BaseTestCase


class TestExtraFieldsInRequestBody(BaseTestCase):
    def test_extra_fields_put_B_200(self):
        self.add_A(id=50)
        self.add_B(id=20, a_id=50)

        response = self.client.open(
            '/api/v1/B/20',
            method='PUT',
            json={
                "a_id": 50,
                "extra_field": "superfluity"
            }
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

    def test_extra_fields_put_C_200(self):
        self.add_C(id=50)

        response = self.client.open(
            '/api/v1/C/50',
            method='PUT',
            json={
                "nullable_column": "new test",
                "extra_field": "superfluity"
            }
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

    def test_extra_fields_put_D_200(self):
        self.add_D(id=50, non_nullable_column='test')

        response = self.client.open(
            '/api/v1/D/50',
            method='PUT',
            json={
                "non_nullable_column": "new test",
                "extra_field": "superfluity"
            }
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
