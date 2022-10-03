# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.tolqc import TolqcTestCase


class TestAuthentication(TolqcTestCase):
    def test_api_key_auth(self):
        good_api_key = {"Authorization": self.api_key_1}
        false_api_key = {"Authorization": "IamAhacker"}

        # no api key
        response = self.client.open(
            '/api/v1/centres',
            method='POST',
            json={
                "data": {
                    "type": "centres",
                    "attributes": {
                        "name": "David",
                        "hierarchy_name": "Hierarchy Tester"
                    }
                },
            }
        )
        self.assert401(response)

        # incorrect api key
        response = self.client.open(
            '/api/v1/centres',
            method='POST',
            json={
                "data": {
                    "type": "centres",
                    "attributes": {
                        "name": "David",
                        "hierarchy_name": "Hierarchy Tester"
                    }
                },
            },
            headers=false_api_key
        )
        self.assert401(response)

        # correct api key
        response = self.client.open(
            '/api/v1/centres',
            method='POST',
            json={
                "data": {
                    "type": "centres",
                    "attributes": {
                        "name": "David",
                        "hierarchy_name": "Hierarchy Tester"
                    }
                },
            },
            headers=good_api_key
        )
        self.assert201(response)
        created_id = response.json['data']['id']
        expect_data = {
            "data": {
                "type": "centres",
                "attributes": {
                    "hierarchy_name": "Hierarchy Tester",
                    "name": "David",
                },
                "id": created_id,
                'relationships': {
                    "runs": {
                        'links': {
                            'related': f'/centres/{created_id}/runs'
                        }
                    }
                }
            }
        }
        self.assertEqual(expect_data, response.json)

        # GET data without api key
        response = self.client.open(
            f'/api/v1/centres/{created_id}',
            method='GET',
        )
        self.assert200(response)
        self.assertEqual(expect_data, response.json)

        # GET data with api key
        response = self.client.open(
            f'/api/v1/centres/{created_id}',
            method='GET',
            headers=good_api_key
        )
        self.assert200(response)
        self.assertEqual(expect_data, response.json)
