# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.base import BaseTestCase


class TestMalformedFilterString(BaseTestCase):
    def test_bad_enclosing_square_brackets_filter_G_400(self):
        self.add_G(id=89890, string_column='test, yet again')
        # no enclosing brackets
        response = self.client.open(
            '/api/v1/G?filter=string_column=="test, yet again"',
            method='GET'
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

        # opening, but not closing
        response = self.client.open(
            '/api/v1/G?filter=[string_column=="test, yet again"',
            method='GET'
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

        # closing, but not opening
        response = self.client.open(
            '/api/v1/G?filter=string_column=="test, yet again"]',
            method='GET'
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

    def test_bad_single_equals_filter_G_400(self):
        self.add_G(id=34788, string_column='tests are fun!!')

        # single instead of double equals sign
        response = self.client.open(
            '/api/v1/G?filter=[string_column="tests are fun!!"]',
            method='GET'
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
