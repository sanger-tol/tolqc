# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.core import BaseTestCase


class TestListResourceIdGiven400(BaseTestCase):
    def test_B_id_given_400_post(self):
        response = self.client.open(
            '/api/v1/B',
            method='POST',
            json={
                "id": 9999,
                "a_id": 0
            }
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
    
    def test_C_id_given_400_post(self):
        pass

    def test_D_id_given_400_post(self):
        pass
