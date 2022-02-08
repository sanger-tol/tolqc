# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.base import BaseTestCase


class TestEnumRelationListGet(BaseTestCase):
    def test_I_relation_on_J_list_get_200(self):
        # add two I's
        self.add_I(id=34091, name='thing1')
        self.add_I(id=981234, name='thing3')
        # add some J's
        self.add_J(id=878934, I='thing3')
        self.add_J(id=98823, I='thing1')
        self.add_J(id=3453290, I='thing1')

        # get thing3's J's
        response = self.client.open(
            '/api/v1/enum/I/thing3/J',
            method='GET'
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        # assert that the correct one is returned
        self.assertEqual(
            response.json,
            {
                'data': [{
                    'type': 'J',
                    'id': '878934',
                    'attributes': {
                        'I': 'thing3'
                    }
                }]
            }
        )

        # get thing1's J's, in descending order of id
        response = self.client.open(
            '/api/v1/enum/I/thing1/J?sort_by=-id',
            method='GET'
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        # assert that the correct one is returned
        self.assertEqual(
            response.json,
            {
                'data': [
                    {
                        'type': 'J',
                        'id': '3453290',
                        'attributes': {
                            'I': 'thing1'
                        }
                    },
                    {
                        'type': 'J',
                        'id': '98823',
                        'attributes': {
                            'I': 'thing1'
                        }
                    }
                ]
            }
        )

    def test_I_bad_name_relation_on_J_list_get_404(self):
        # add an I
        self.add_I(id=98902, name='thing2')
        # try to get the J's of a non-existent I
        response = self.client.open(
            '/api/v1/enum/I/nothing/J',
            method='GET'
        )
        self.assert404(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        # assert that it failed for the right reason
        self.assertEqual(
            response.json,
            {
                'errors': [{
                    'title': 'Not Found',
                    'code': 404,
                    'detail': "No name 'nothing' exists on enum I."
                }]
            }
        )
