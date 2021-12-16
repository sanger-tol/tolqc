# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from . import BaseTestCase
from main.model import db


api_key = {"Authorization": "AnyThingBecAuseThIsIsATEST567890"}
false_api_key = {"Authorization": "IamAhacker"}


class TestAuthentication(BaseTestCase):
    def test_api_key_auth(self):
        db.engine.execute("ALTER SEQUENCE centre_id_seq RESTART WITH 1;")

        # no api key
        response = self.client.open(
            '/api/v1/centres',
            method='POST',
            json=[{
                "name": "David",
                "hierarchy_name": "Hierarchy Tester"
            }],
        )
        self.assert401(response)

        # incorrect api key
        response = self.client.open(
            '/api/v1/centres',
            method='POST',
            json=[{
                "name": "David",
                "hierarchy_name": "Hierarchy Tester"
            }],
            headers=false_api_key
        )
        self.assert401(response)

        # correct api key
        response = self.client.open(
            '/api/v1/centres',
            method='POST',
            json=[{
                "name": "David",
                "hierarchy_name": "Hierarchy Tester"
            }],
            headers=api_key
        )
        expect_data = {
            "hierarchy_name": "Hierarchy Tester",
            "name": "David",
            "created_at": response.json['data'][0]['attributes']['created_at'],
            "created_by": 100
        }
        expect_errors = [None]
        self.assert200(response)
        self.assertEqual(expect_data, response.json['data'][0]['attributes'])
        self.assertEqual(expect_errors, response.json['meta']['errors'])

        # GET data without api key
        id = response.json['data'][0]['id']
        response = self.client.open(
            f'/api/v1/centres/{id}',
            method='GET',
        )
        expect_data = {
            "data": {
              "type": "centre",
              "attributes": {
                "hierarchy_name": "Hierarchy Tester",
                "name": "David",
                "created_at": response.json['data']['attributes']['created_at'],
                "created_by": 100
              },
              "id": 1
            }
        }
        self.assert200(response)
        self.assertEqual(expect_data, response.json)

        # GET data with api key
        response = self.client.open(
            '/api/v1/centres/1',
            method='GET',
            headers=api_key
        )
        self.assert200(response)
        self.assertEqual(expect_data, response.json)
