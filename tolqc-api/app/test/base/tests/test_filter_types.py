# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.base import BaseTestCase


class TestFilterTypes(BaseTestCase):
    def test_string_bad_delimiter_list_get_G_400(self):
        self.add_G(id=1001)

        # undelimited string
        response = self.client.open(
            '/api/v1/G?filter=[string_column==undelimited]'
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

        # unmatching delimiters
        response = self.client.open(
            '/api/v1/G?filter=[string_column==\'unmatching"]'
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

    def test_string_good_delimiters_list_get_G_200(self):
        self.add_G(id=101, string_column="match", bool_column=True)
        self.add_G(id=1090, string_column="no match", bool_column=False)

        response = self.client.open(
            '/api/v1/G?filter=[string_column=="match"]'
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
    
        # check only 1 retrieved result
        self.assertEqual(len(response.json['data']), 1)

        # confirm it's the correct one
        self.assertEqual(
            response.json,
            {
                'data': [
                    {
                        'type': 'G',
                        'id': '101',
                        'attributes': {
                            'float_column': None,
                            'bool_column': True,
                            'datetime_column': None,
                            'string_column': 'match'
                        }
                    }
                ]
            }
        )
