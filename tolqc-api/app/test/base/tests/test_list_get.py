# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.base import BaseTestCase


class TestListGet(BaseTestCase):
    def test_get_multiple_inserted_C(self):
        c_1 = {
            "id": 9090,
        }
        c_2 = {
            "id": 80808,
            "nullable_column": "hello, how are you"
        }
        c_3 = {
            "id": 989089,
            "other_column": "fine, and yourself?"
        }
        self.add_C(**c_1)
        self.add_C(**c_2)
        self.add_C(**c_3)

        response = self.client.open(
            '/api/v1/C',
            method='GET'
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        self.assertEqual(
            response.json,
            {
                'data': [
                    {
                        'type': 'C',
                        'id': '9090',
                        'attributes': {
                            'nullable_column': None,
                            'other_column': None
                        }
                    },
                    {
                        'type': 'C',
                        'id': '80808',
                        'attributes': {
                            'nullable_column': "hello, how are you",
                            'other_column': None
                        }
                    },
                    {
                        'type': 'C',
                        'id': '989089',
                        'attributes': {
                            'nullable_column': None,
                            'other_column': "fine, and yourself?"
                        }
                    },
                ]
            }
        )

    def test_paged_correct_quantity(self):
        for i in range(47):
            self.add_C(
                id=i,
                nullable_column="attack of the clones"
            )

        # (implictly) first page
        response = self.client.open(
            '/api/v1/C',
            method='GET'
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        # should be fully populated 
        self.assertEqual(len(response.json['data']), 20)

        # last (partially) populated page
        response = self.client.open(
            '/api/v1/C?page=3',
            method='GET'
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        # 7 = 47 - 20*2
        self.assertEqual(len(response.json['data']), 7)

        # obviously out of range page
        response = self.client.open(
            '/api/v1/C?page=9999',
            method='GET'
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        # should not be populated at all
        self.assertEqual(len(response.json['data']), 0)
