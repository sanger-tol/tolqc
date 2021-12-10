# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.core import BaseTestCase


class TestIdInRequestBody(BaseTestCase):
    # TODO these tests are passing for the wrong reason, fix!
    def test_B_id_in_request_body_post_400(self):
        response = self.client.open(
            '/api/v1/B',
            method='POST',
            json=[{
                "id": 9999,
                "a_id": 0
            }]
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        errors = response.json['meta']['errors']
        self.assertEqual(len(errors), 1)
        self.assertNotEqual(errors[0], None)

    def test_C_id_in_request_body_post_error(self):
        response = self.client.open(
            '/api/v1/C',
            method='POST',
            json=[{
                "id": 9999,
                "nullable_column": "doesn't matter"
            }]
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        errors = response.json['meta']['errors']
        self.assertEqual(len(errors), 1)
        self.assertNotEqual(errors[0], None)

    def test_D_id_in_request_body_post_error(self):
        response = self.client.open(
            '/api/v1/D',
            method='POST',
            json=[{
                "id": 9999,
                "non_nullable_column": "Not at all"
            }]
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

        errors = response.json['meta']['errors']
        self.assertEqual(len(errors), 1)
        self.assertNotEqual(errors[0], None)

    def test_B_id_in_request_body_put_400(self):
        response = self.client.open(
            '/api/v1/B/70',
            method='PUT',
            json={
                "id": 9999
            }
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

    def test_C_id_in_request_body_put_400(self):
        response = self.client.open(
            '/api/v1/B/70',
            method='PUT',
            json={
                "id": 9999
            }
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

    def test_D_id_in_request_body_put_400(self):
        response = self.client.open(
            '/api/v1/D/70',
            method='PUT',
            json={
                "id": 9999
            }
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
