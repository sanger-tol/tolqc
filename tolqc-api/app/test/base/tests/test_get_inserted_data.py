# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.base import BaseTestCase


class TestGetInsertedData(BaseTestCase):
    def test_get_inserted_B_200(self):
        self.add_A(id=90)
        self.add_B(id=10, a_id=90)

        expected = {
            'data': {
                'type': 'B',
                'id': '10',
                'relationships': {
                    'A': {
                        'data': {
                            'id': '90',
                            'type': 'A'
                        },
                        'links': {
                            'related': '/A/90'
                        }
                    },
                    'E': {
                        'links': {
                            'related': '/B/10/E'
                        }
                    }
                }
            }
        }

        response = self.client.open(
            '/api/v1/B/10',
            method='GET',
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        self.assertEqual(expected, response.json)

    def test_get_inserted_C_200(self):
        self.add_C(id=9, other_column='test the world')

        expected = {
            'data': {
                'id': '9',
                'type': 'C',
                'attributes': {
                    'nullable_column': None,
                    'other_column': 'test the world',
                }
            }
        }

        response = self.client.open(
            '/api/v1/C/9',
            method='GET',
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        self.assertEqual(expected, response.json)

    def test_get_inserted_D_200(self):
        self.add_D(
            id=1122,
            non_nullable_column='This shouldnt be null',
            other_column='This, however, can be null!',
        )

        expected = {
            'data': {
                'id': '1122',
                'type': 'D',
                'attributes': {
                    "non_nullable_column": 'This shouldnt be null',
                    "other_column": 'This, however, can be null!',
                }
            }
        }
        response = self.client.open(
            '/api/v1/D/1122',
            method='GET',
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        self.assertEqual(expected, response.json)
