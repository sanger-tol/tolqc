# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.core import BaseTestCase
from test.core.models import ModelRelationshipB, \
                             ModelWithNullableColumn, \
                             ModelWithNonNullableColumn


class TestUpdatedCorrectly200(BaseTestCase):
    def test_updated_correctly_B_200(self):
        a_id = 109
        new_a_id = 9090
        b_id = 218
        self.add_A(id=a_id)
        self.add_A(id=new_a_id)
        self.add_B(id=b_id, a_id=a_id)

        response = self.client.open(
            f'/api/v1/B/{b_id}',
            method='PUT',
            json={
                'a_id': new_a_id,
            }
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

        updated = ModelRelationshipB.find_by_id(b_id)
        self.assertEqual(updated.a_id, new_a_id)

    def test_updated_correctly_C_200(self):
        self.add_C(id=9087)
        new_other_column_string = 'this is a test, nice'

        response = self.client.open(
            '/api/v1/C/9087',
            method='PUT',
            json={
                'other_column': new_other_column_string
            }
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

        updated = ModelWithNullableColumn.find_by_id(9087)
        self.assertEqual(updated.nullable_column, None)
        self.assertEqual(updated.other_column, new_other_column_string)

    def test_updated_correctly_D_200(self):
        new_other_column_string = 'this is also a test'
        new_non_nullable_string = 'another test, sick'
        self.add_D(id=919191, non_nullable_column='eep')

        response = self.client.open(
            '/api/v1/D/919191',
            method='PUT',
            json={
                'other_column': new_other_column_string,
                'non_nullable_column': new_non_nullable_string
            }
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

        updated = ModelWithNonNullableColumn.find_by_id(919191)
        self.assertEqual(
            updated.non_nullable_column,
            new_non_nullable_string
        )
        self.assertEqual(updated.other_column, new_other_column_string)
