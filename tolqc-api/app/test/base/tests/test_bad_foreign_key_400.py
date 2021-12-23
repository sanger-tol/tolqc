# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.base import BaseTestCase


class TestBadForeignKey400(BaseTestCase):
    def test_post_B_with_bad_foreign_key_error(self):
        self.add_A(id=20)

        import logging#reeemove
        from test.base.schemas import B_Schema
        logging.warning(B_Schema.get_excluded_columns())

        response = self.client.open(
            '/api/v1/B',
            method='POST',
            json={
                "data": {
                    "type": 'B',
                    "attributes": {},
                    "relationships": {
                        "test_A": {
                            "data": {
                                "type": 'A',
                                "id": 9999
                            }
                        }
                    }
                }
            },
            headers=self._get_api_key()
        )
        self.assert400(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

