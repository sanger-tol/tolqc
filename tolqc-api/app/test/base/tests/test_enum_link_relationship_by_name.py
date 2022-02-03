# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.base import BaseTestCase


class TestEnumLinkRelationshipByName(BaseTestCase):
    def _assert_enum_validation_error(self, response):
        errors = response.json.get('errors', [])
        first_error = {} if not errors else errors[0]
        error_title = first_error.get('title', None)
        self.assertEqual(
            error_title,
            'Validation Error'
        )

    def test_post_J_specify_I_by_name(self):
        self.add_I(id=4857, name='nicely')
        response = self.client.open(
            '/api/v1/J',
            method='POST',
            headers=self._get_api_key_1(),
            json={
                'data': {
                    'type': 'J',
                    'attributes': {
                        'I': 'nicely'
                    }
                }
            }
        )
        self.assert201(response)

        # get non predictable id
        created_id = response.json['data']['id']

        # assert response json is correct
        self.assertEqual(
            response.json,
            {
                'data': {
                    'type': 'J',
                    'id': created_id,
                    'attributes': {
                        'I': 'nicely'
                    }
                }
            }
        )
