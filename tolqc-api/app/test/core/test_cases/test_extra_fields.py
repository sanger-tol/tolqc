# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.core import BaseTestCase
from test.core.models import ModelRelationshipA, \
                             ModelWithExtField


class TestExtraFieldsInRequestBody(BaseTestCase):
    def test_ext_field_does_not_exist_A(self):
        self.assertEqual(
            ModelRelationshipA.has_ext_column(),
            False
        )

    def test_ext_field_exists_F(self):
        self.assertEqual(
            ModelWithExtField.has_ext_column(),
            True
        )

    def test_extra_fields_post_F_200(self):
        extra_fields = {
            "extra_field": "superfluity",
            "another_ext": "Yet another extra field"
        }
        response = self.client.open(
            '/api/v1/F',
            method='POST',
            json={
                **extra_fields,
                "other_column": "another test :("
            }
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

        id = response.json['data']['id']
        F_instance = ModelWithExtField.find_by_id(id)
        self.assertEqual(F_instance.ext, extra_fields)
        self.assertEqual(F_instance.other_column, "another test :(")

    def test_no_extra_fields_post_F_200(self):
        response = self.client.open(
            '/api/v1/F',
            method='POST',
            json={
                "other_column": "nonsense!!!"
            }
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

        id = response.json['data']['id']
        F_instance = ModelWithExtField.find_by_id(id)
        self.assertEqual(F_instance.other_column, "nonsense!!!")
        self.assertEqual(F_instance.ext, None)

    def test_extra_fields_put_B_400(self):
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
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

    def test_extra_fields_put_C_400(self):
        self.add_C(id=50)

        response = self.client.open(
            '/api/v1/C/50',
            method='PUT',
            json={
                "nullable_column": "new test",
                "extra_field": "superfluity"
            }
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

    def test_extra_fields_put_D_400(self):
        self.add_D(id=50, non_nullable_column='test')

        response = self.client.open(
            '/api/v1/D/50',
            method='PUT',
            json={
                "non_nullable_column": "new test",
                "extra_field": "superfluity"
            }
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
    
    def test_extra_fields_post_D_400(self):
        response = self.client.open(
            '/api/v1/D',
            method='POST',
            json={
                "non_nullable_column": "new test",
                "extra_field": "superfluity"
            }
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
