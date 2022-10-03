# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.base import BaseTestCase


class TestDeleteWithDependant400(BaseTestCase):
    def test_delete_B_with_dependant_E_400(self):
        self.add_A(id=20)
        self.add_B(id=30, a_id=20)
        self.add_E(id=40, b_id=30)

        response = self.client.open(
            '/api/v1/B/30',
            method='DELETE',
            headers=self._get_api_key_1_headers()
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
