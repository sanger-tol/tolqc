# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.base import BaseTestCase


class TestEnumMethodsByName(BaseTestCase):
    def test_I_get_by_name_matches_by_id_200(self):
        self.add_I(id=348598, name='testing')
        # get by id
        response_by_id = self.client.open(
            '/api/v1/I/348598',
            method='GET'
        )
        self.assert200(
            response_by_id,
            f'Response body is : {response_by_id.data.decode("utf-8")}'
        )
        # assert that the response is correct
        self.assertEqual(
            response_by_id.json,
            {
                'data': {
                    'type': 'I',
                    'id': '348598',
                    'attributes': {
                        'name': 'testing',
                        'description': None
                    }
                }
            }
        )    
