# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.core import BaseTestCase
from test.core.models import ModelRelationshipB, \
                             ModelWithNullableColumn, \
                             ModelWithNonNullableColumn

# TODO check multiple inserts
class TestInsertedCorrectly200(BaseTestCase):
    def test_inserted_correctly_B_200(self):
        a_id = 90
        self.add_A(id=a_id)

        response = self.client.open(
            '/api/v1/B',
            method='POST',
            json=[{
                'a_id': a_id,
            }]
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        self.assertEqual(response.json['meta']['errors'], [None])
        id = response.json['data'][0]['id']

        inserted = ModelRelationshipB.find_by_id(id)
        self.assertEqual(inserted.a_id, a_id)

    def test_inserted_correctly_C_200(self):
        other_column_string = 'this is a test, nice'

        response = self.client.open(
            '/api/v1/C',
            method='POST',
            json={
                'other_column': other_column_string
            }
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        id = response.json['data']['id']

        inserted = ModelWithNullableColumn.find_by_id(id)
        self.assertEqual(inserted.nullable_column, None)
        self.assertEqual(inserted.other_column, other_column_string)

    def test_inserted_correctly_D_200(self):
        other_column_string = 'this is also a test'
        non_nullable_string = 'another test, sick'

        response = self.client.open(
            '/api/v1/D',
            method='POST',
            json={
                'other_column': other_column_string,
                'non_nullable_column': non_nullable_string
            }
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        id = response.json['data']['id']

        inserted = ModelWithNonNullableColumn.find_by_id(id)
        self.assertEqual(
            inserted.non_nullable_column,
            non_nullable_string
        )
        self.assertEqual(inserted.other_column, other_column_string)
