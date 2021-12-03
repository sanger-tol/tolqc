# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask_sqlalchemy.model import Model
from test.core import BaseTestCase
from test.core.models import ModelRelationshipB


class TestInsertedCorrectly200(BaseTestCase):
    def test_inserted_correctly_B_200(self):
        a_id=90
        self.add_A(id=a_id)

        response = self.client.open(
            '/api/v1/B',
            method='POST',
            json={
                'a_id': a_id,
            }
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        id = response.json['data']['id']

        inserted = ModelRelationshipB.find_by_id(id)
        self.assertEqual(inserted.a_id, a_id)