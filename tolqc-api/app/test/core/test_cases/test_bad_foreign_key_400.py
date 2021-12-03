# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.core import BaseTestCase


class TestBadForeignKey400(BaseTestCase):
    def test_post_B_with_bad_foreign_key_400(self):
        self.add_A(id=20)

        response = self.client.open(
            '/api/v1/B',
            method='POST',
            json={
                "a_id": 9999
            }
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
