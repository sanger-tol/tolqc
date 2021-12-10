# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.core import BaseTestCase


class TestSpecifyExtInRequestError(BaseTestCase):
    def test_specify_ext_post_F_error(self):
        response = self.client.open(
            '/api/v1/F',
            method='POST',
            json=[{
                "ext": {"test": "test"}
            }]
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        errors = response.json['meta']['errors']
        self.assertEqual(len(errors), 1)
        self.assertNotEqual(errors[0], None)

    # TODO implement for PUT
