# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.base import BaseTestCase


class TestRelationListGet(BaseTestCase):
    def test_relation_list_get_A_B_200(self):
        #TODO add one to many relationships in both output and swagger models
        #TODO test all parameters (list get) on relation list get
        # add two A's
        self.add_A(id=20)
        self.add_A(id=29)

        # add two B's on the first A
        self.add_B(id=89, a_id=20)
        self.add_B(id=290, a_id=20)

        # add one B on the second A
        self.add_B(id=8080, a_id=29)

        # get the first A's B's
        response = self.client.open(
            '/api/v1/A/20/B',
            method='GET'
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        # assert that 2 were found
        self.assertEqual(len(response.json['data']), 2)
        # assert that the correct two were found
        self.assertEqual(
            response.json,
            {
                'data': [
                    {
                        'id': '89',
                        'type': 'B',
                        'relationships': {
                            'A': {
                                'data': {
                                    'id': '20',
                                    'type': 'A'
                                },
                                'links': {
                                    'related': '/A/20'
                                }
                            }
                        }
                    },
                    {
                        'id': '290',
                        'type': 'B',
                        'relationships': {
                            'A': {
                                'data': {
                                    'id': '20',
                                    'type': 'A'
                                },
                                'links': {
                                    'related': '/A/20'
                                }
                            }
                        }
                    }
                ]
            }
        )

        # get the second A's B
        response = self.client.open(
            '/api/v1/A/29/B',
            method='GET'
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        # assert that 1 was found
        self.assertEqual(len(response.json['data']), 1)
        # assert that the correct one was found
        self.assertEqual(
            response.json,
            {
                'data': [
                    {
                        'id': '8080',
                        'type': 'B',
                        'relationships': {
                            'A': {
                                'data': {
                                    'id': '29',
                                    'type': 'A'
                                },
                                'links': {
                                    'related': '/A/29'
                                }
                            }
                        }
                    }
                ]
            }
        )

    def test_relation_list_get_no_stem_A_B_404(self):
        # add an irrelevant A and connected B
        self.add_A(id=99)
        self.add_B(id=100, a_id=99)

        # try to get the B's of a non-existent A
        response = self.client.open(
            '/api/v1/A/560/B',
            method='GET'
        )
        self.assert404(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
