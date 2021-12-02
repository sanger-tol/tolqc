# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.core import BaseTestCase


class TestGetInsertedData(BaseTestCase):
    def test_get_inserted_B(self):
        self.add_A(id=90)
        self.add_B(id=10, a_id=90)

        expected = self.to_json_api(
            10,
            'B',
            {
                "a_id": 90,
            },
        )

        response = self.client.open(
            '/api/v1/B/10',
            method='GET',
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        self.assertEqual(expected, response.json)
    
    def test_get_inserted_C(self):
        self.add_C(id=9, other_column='test the world')

        expected = self.to_json_api(
            9, 
            'C',
            {
                'nullable_column': None,
                'other_column': 'test the world',
            }
        )
        
        response = self.client.open(
            '/api/v1/C/9',
            method='GET',
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        self.assertEqual(expected, response.json)
    
    def test_get_inserted_D(self):
        self.add_D(
            id=1122,
            non_nullable_column='This shouldnt be null',
            other_column='This, however, can be null!',
        )

        expected = self.to_json_api(
            1122,
            'D',
            {
                "non_nullable_column": 'This shouldnt be null',
                "other_column": 'This, however, can be null!',
            }
        )

        response = self.client.open(
            '/api/v1/D/1122',
            method='GET',
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        self.assertEqual(expected, response.json)
