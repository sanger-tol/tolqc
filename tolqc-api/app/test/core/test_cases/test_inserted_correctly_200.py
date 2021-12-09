# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.core import BaseTestCase
from test.core.models import ModelRelationshipB, \
                             ModelWithNullableColumn, \
                             ModelWithNonNullableColumn

# TODO check multiple inserts
class TestInsertedCorrectly(BaseTestCase):
    def test_inserted_correctly_B(self):
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

    def test_multiple_inserted_correctly_C_200(self):
        response = self.client.open(
            '/api/v1/C',
            method='POST',
            json=[{
                'other_column': 'this is a test, nice'
            }, {
                'other_column': 'another test',
                'nullable_column': 'nothing to see here'
            }]
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

        self.assertEqual(response.json['meta']['errors'], [None, None])

        id_0 = response.json['data'][0]['id']
        inserted_0 = ModelWithNullableColumn.find_by_id(id_0)
        self.assertEqual(inserted_0.nullable_column, None)
        self.assertEqual(inserted_0.other_column, 'this is a test, nice')

        id_1 = response.json['data'][1]['id']
        inserted_1 = ModelWithNullableColumn.find_by_id(id_1)
        self.assertEqual(inserted_1.nullable_column, 'nothing to see here')
        self.assertEqual(inserted_1.other_column, 'another test')

    def test_inserted_correctly_D_200(self):
        other_column_string = 'this is also a test'
        non_nullable_string = 'another test, sick'

        response = self.client.open(
            '/api/v1/D',
            method='POST',
            json=[{
                'other_column': other_column_string,
                'non_nullable_column': non_nullable_string
            }]
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

        self.assertEqual(response.json['meta']['errors'], [None])

        id = response.json['data'][0]['id']
        inserted = ModelWithNonNullableColumn.find_by_id(id)
        self.assertEqual(
            inserted.non_nullable_column,
            non_nullable_string
        )
        self.assertEqual(inserted.other_column, other_column_string)
    
    def partial_insertion_success_F(self):
        pass
