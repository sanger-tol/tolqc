# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from datetime import datetime

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

    def test_float_filter_correct_list_get_G_200(self):
        self.add_G(id=501, string_column="laughter", float_column=9.16)
        self.add_G(id=17890, string_column="good medicine", float_column=1.89)

        # filter for one
        response = self.client.open(
            '/api/v1/G?filter=[float_column==1.89]'
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

        # check only 1 retrieved result
        self.assertEqual(len(response.json['data']), 1)

        # check the result is the correct one
        self.assertEqual(
            response.json,
            {
                'data': [
                    {
                        'type': 'G',
                        'id': '17890',
                        'attributes': {
                            'float_column': 1.89,
                            'bool_column': None,
                            'datetime_column': None,
                            'string_column': "good medicine"
                        }
                    }
                ]
            }
        )

        # filter for none
        response = self.client.open(
            '/api/v1/G?filter=[float_column==42.9]'
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        # assert no results
        self.assertEqual(
            response.json,
            {
                'data': []
            }
        )

    def test_datetime_filter_correct_list_get_G_200(self):
        first_datetime = datetime.now()
        second_datetime = datetime.now()
        self.add_G(id=501, string_column="hamburger", datetime_column=first_datetime)
        self.add_G(id=17890, string_column="cat", datetime_column=second_datetime)

        # filter for none
        response = self.client.open(
            f'/api/v1/G?filter=[datetime_column=={str(datetime.now())}]'
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        # assert no results
        self.assertEqual(
            response.json,
            {
                'data': []
            }
        )

        # filter for one
        response = self.client.open(
            f'/api/v1/G?filter=[datetime_column=={str(first_datetime)}]'
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        # one result, and is correct
        self.assertEqual(len(response.json['data']), 1)
        self.assertEqual(
            response.json,
            {
                'data': [
                    {
                        'type': 'G',
                        'id': '501',
                        'attributes': {
                            'float_column': None,
                            'bool_column': None,
                            'datetime_column': first_datetime.strftime(
                                '%Y-%m-%dT%H:%M:%S.%f'
                            ),
                            'string_column': 'hamburger'
                        }
                    }
                ]
            }
        )

    def test_multiple_filters_correct_list_get_C_200(self):
        # testing bool and float
        self.add_G(id=999, float_column=1.0, bool_column=True)
        self.add_G(id=1021, float_column=49584.0, bool_column=True)
        self.add_G(id=34989, float_column=1.0, bool_column=False)

        # get none
        response = self.client.open(
            '/api/v1/G?filter=[float_column==898.34,bool_column==True]'
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        self.assertEqual(len(response.json['data']), 0)

        # get one
        response = self.client.open(
            '/api/v1/G?filter=[float_column==1.0,bool_column==True]'
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        self.assertEqual(len(response.json['data']), 1)
        self.assertEqual(
            response.json,
            {
                'data': [
                    {
                        'type': 'G',
                        'id': '999',
                        'attributes': {
                            'float_column': 1.0,
                            'bool_column': True,
                            'datetime_column': None,
                            'string_column': None
                        }
                    }
                ]
            }
        )
