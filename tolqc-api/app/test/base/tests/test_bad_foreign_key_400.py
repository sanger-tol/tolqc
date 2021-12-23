# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.base import BaseTestCase


class TestBadForeignKey400(BaseTestCase):
    def test_post_B_with_bad_foreign_key_error(self):
        self.add_A(id=20)

        response = self.client.open(
            '/api/v1/B',
            method='POST',
            json={
                "data": {
                    "type": 'B',
                    "attributes": {},
                    "relationships": {
                        "A": {
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
    
    def test_fail(self):
        from test.base.models import B_ModelRelationship
        import logging
        stuff = B_ModelRelationship.get_foreign_key_column_names()
        logging.warning(B_ModelRelationship.get_relationship_from_foreign_key(stuff[0]))
        relationships_dict = B_ModelRelationship.get_relationships_dict()
        self.assertEqual(False, True)

