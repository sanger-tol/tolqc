# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.base import BaseTestCase


class TestRelationListGet(BaseTestCase):
    def test_relation_list_get_A_B_200(self):
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
                            },
                            "E": {
                                'links': {
                                    'related': '/B/89/E'
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
                            },
                            "E": {
                                'links': {
                                    'related': '/B/290/E'
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
                            },
                            "E": {
                                'links': {
                                    'related': '/B/8080/E'
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

    def test_relation_list_get_with_page_parameter_200(self):
        """Confirm that the page parameter works with a relation
        list get endpoint"""
        # add an A
        self.add_A(id=789)

        # add 59 B's
        for i in range (1, 60):
            self.add_B(id=i, a_id=789)
        
        # combine parameters on relation list get
        response = self.client.open(
            '/api/v1/A/789/B?page=3',
            method='GET'
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        # 19 = 59 - 20*2
        self.assertEqual(len(response.json['data']), 19)

    def test_relation_list_get_with_sortby_parameter_200(self):
        # add an A
        self.add_A(id=298)

        # add 3 B's in no particular order
        self.add_B(id=9090, a_id=298)
        self.add_B(id=348, a_id=298)
        self.add_B(id=200000, a_id=298)

        # combine parameters on relation list get
        response = self.client.open(
            '/api/v1/A/298/B?sort_by=-id',
            method='GET'
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        self.assertEqual(len(response.json['data']), 3)
        # assert they're in the right order (descending id)
        self.assertEqual(
            response.json,
            {
                'data': [
                    {
                        'id': '200000',
                        'type': 'B',
                        'relationships': {
                            'A': {
                                'data': {
                                    'id': '298',
                                    'type': 'A'
                                },
                                'links': {
                                    'related': '/A/298'
                                }
                            },
                            "E": {
                                'links': {
                                    'related': '/B/200000/E'
                                }
                            }
                        }
                    },
                    {
                        'id': '9090',
                        'type': 'B',
                        'relationships': {
                            'A': {
                                'data': {
                                    'id': '298',
                                    'type': 'A'
                                },
                                'links': {
                                    'related': '/A/298'
                                }
                            },
                            "E": {
                                'links': {
                                    'related': '/B/9090/E'
                                }
                            }
                        }
                    },
                    {
                        'id': '348',
                        'type': 'B',
                        'relationships': {
                            'A': {
                                'data': {
                                    'id': '298',
                                    'type': 'A'
                                },
                                'links': {
                                    'related': '/A/298'
                                }
                            },
                            "E": {
                                'links': {
                                    'related': '/B/348/E'
                                }
                            }
                        }
                    }
                ]
            }
        )