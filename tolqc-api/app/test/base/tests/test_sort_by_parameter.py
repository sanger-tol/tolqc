# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.base import BaseTestCase


class TestBadSortByParameter200(BaseTestCase):
    def test_no_sort_by_key_200(self):
        self.add_D(id=890, non_nullable_column='a nice test')
        response = self.client.open(
            '/api/v1/D?sort_by=',
            method='GET'
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        self.assertEqual(len(response.json['data']), 1)

    def test_sort_by_default_id_ascending_200(self):
        self.add_C(id=89)
        self.add_C(id=39489)
        self.add_C(id=768)
        self.add_C(id=78)

        # no sort_by parameter specified
        response = self.client.open(
            '/api/v1/C',
            method='GET'
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        self.assertEqual(len(response.json['data']), 4)

        # in correct (ascending) order of id
        self.assertEqual(
            response.json,
            {
                'data': [
                    {
                        'type': 'C',
                        'id': '78',
                        'attributes': {
                            'nullable_column': None,
                            'other_column': None
                        }
                    },
                    {
                        'type': 'C',
                        'id': '89',
                        'attributes': {
                            'nullable_column': None,
                            'other_column': None
                        }
                    },
                    {
                        'type': 'C',
                        'id': '768',
                        'attributes': {
                            'nullable_column': None,
                            'other_column': None
                        }
                    },
                    {
                        'type': 'C',
                        'id': '39489',
                        'attributes': {
                            'nullable_column': None,
                            'other_column': None
                        }
                    },
                ]
            }
        )

    def test_sort_by_and_filter_200(self):    
        self.add_G(id=90909, bool_column=True)
        self.add_G(id=45878, bool_column=False)
        self.add_G(id=7482, bool_column=True)

        # filter for two, sort by id descending
        response = self.client.open(
            '/api/v1/G?sort_by=-id&filter=[bool_column==true]',
            method='GET'
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        self.assertEqual(len(response.json['data']), 2)

        # assert the two matches are in order, by descending id
        self.assertEqual(
            response.json,
            {
                'data': [
                    {
                        'type': 'G',
                        'id': '90909',
                        'attributes': {
                            'float_column': None,
                            'datetime_column': None,
                            'bool_column': True,
                            'string_column': None
                        } 
                    },
                    {
                        'type': 'G',
                        'id': '7482',
                        'attributes': {
                            'float_column': None,
                            'datetime_column': None,
                            'bool_column': True,
                            'string_column': None
                        } 
                    }
                ]
            }
        )
