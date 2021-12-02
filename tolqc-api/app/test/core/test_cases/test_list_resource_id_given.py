# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.core import BaseTestCase


class TestListResourceIdGiven(BaseTestCase):
    def test_id_given_B_post_405(self):
        response = self.client.open(
            '/api/v1/B/9999',
            method='POST',
        )
        self.assert405(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

    def test_id_given_C_post_405(self):
        response = self.client.open(
            '/api/v1/C/9999',
            method='POST',
        )
        self.assert405(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

    def test_id_given_D_post_405(self):
        response = self.client.open(
            '/api/v1/D/9999',
            method='POST',
        )
        self.assert405(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
