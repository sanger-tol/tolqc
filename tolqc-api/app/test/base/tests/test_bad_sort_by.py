# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.base import BaseTestCase


class TestBadSortByParameter400(BaseTestCase):
    def test_no_sort_by_invalid_key_400(self):
        self.add_D(id=890, non_nullable_column='a nice test')
        response = self.client.open(
            '/api/v1/D?sort_by=invalid_column',
            method='GET'
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
