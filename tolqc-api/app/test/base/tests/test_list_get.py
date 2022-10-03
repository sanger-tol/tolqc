# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.base import BaseTestCase


class TestListGet(BaseTestCase):
    def test_get_multiple_inserted_C_200(self):
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

    def test_paged_correct_quantity_C_200(self):
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

        # first unpopulated page
        response = self.client.open(
            '/api/v1/C?page=4',
            method='GET'
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        self.assertEqual(len(response.json['data']), 0)

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

    def test_quantity_all_parameters_simultaneously_get_C_200(self):
        # add 50 C's, half of which the filter should match
        for i in range(50):
            self.add_C(
                id=i,
                nullable_column="monoclonal antibodies"
                if i % 2 == 0
                else "something about clones"
            )

        response = self.client.open(
            '/api/v1/C?page=2&sort_by=-nullable_column&filter='
            '[nullable_column=="something about clones"]',
            method='GET'
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        # 5 = 50/2 - 20
        self.assertEqual(len(response.json['data']), 5)

    def test_bad_page_get_C_400(self):
        self.add_C(
            id=100,
            nullable_column="test not clone"
        )

        # out of range page
        response = self.client.open(
            '/api/v1/C?page=0',
            method='GET'
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

        # non int page
        response = self.client.open(
            '/api/v1/C?page=not_int',
            method='GET'
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
