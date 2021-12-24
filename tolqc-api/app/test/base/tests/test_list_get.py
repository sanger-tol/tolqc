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
        self.assert200(response)
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
