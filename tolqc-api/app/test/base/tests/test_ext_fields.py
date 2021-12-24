# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.base import BaseTestCase
from test.base.models import A_ModelRelationship, \
                             F_ModelWithExtField


class TestExtraFieldsInRequestBody(BaseTestCase):
    def test_ext_field_does_not_exist_A(self):
        self.assertEqual(
            A_ModelRelationship.has_ext_column(),
            False
        )

    def test_ext_field_exists_F(self):
        self.assertEqual(
            F_ModelWithExtField.has_ext_column(),
            True
        )

    def test_extra_fields_post_F_201(self):
        extra_fields = {
            "extra_field": "superfluity",
            "another_ext": "Yet another extra field"
        }
        response = self.client.open(
            '/api/v1/F',
            method='POST',
            json={
                'data': {
                    'type': 'F',
                    'meta': {
                        'ext': extra_fields
                    }
                }
            },
            headers=self._get_api_key()
        )
        self.assert201(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

        id = response.json['data']['id']
        self.assertEqual(
            response.json,
            {
                'data': {
                    'type': 'F',
                    'id': id,
                    'attributes': {
                        'other_column': None
                    },
                    'meta': {
                        'ext': extra_fields
                    }
                }
            }
        )
        F_instance = F_ModelWithExtField.find_by_id(id)
        self.assertEqual(F_instance.ext, extra_fields)
    
    def test_no_extra_fields_post_F_201(self):
        response = self.client.open(
            '/api/v1/F',
            method='POST',
            json={
                'data': {
                    'type': 'F',
                    'attributes': {
                        'other_column': 'nice test'
                    }
                }
            },
            headers=self._get_api_key()
        )
        self.assert201(response)
    
        id = response.json['data']['id']
        self.assertEqual(
            response.json,
            {
                'data': {
                    'type': 'F',
                    'attributes': {
                        'other_column': 'nice test'
                    },
                    'id': id,
                    'meta': {
                        'ext': {}
                    }
                }
            }
        )
        F_instance = F_ModelWithExtField.find_by_id(id)
        self.assertEqual(F_instance.ext, {})

    def test_extra_fields_patch_B_400(self):
        self.add_A(id=50)
        self.add_B(id=20, a_id=50)

        response = self.client.open(
            '/api/v1/B/20',
            method='PATCH',
            json={
                'data': {
                    'type': 'B',
                    'attributes': {},
                    'meta': {
                        'ext': {
                            'extra_field': 'superfluity'
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
    
    def test_no_extra_fields_get_F_200(self):
        self.add_F(id=290)

        response = self.client.open(
            '/api/v1/F/290',
            method='GET'
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )

        self.assertEqual(
            response.json,
            {
                'data': {
                    'type': 'F',
                    'id': '290',
                    'attributes': {
                        'other_column': None
                    },
                    'meta': {
                        'ext': {}
                    }
                }
            }
        )
    
    def test_variety_type_extra_fields_get_F_200(self):
        ext_data = {
            "arrayData": [27, {
                "testElement": "123"
            }],
            "float": 9090.248,
            "null": [None]
        }
        self.add_F(id=297, ext=ext_data)

        response = self.client.open(
            '/api/v1/F/297',
            method='GET'
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        self.assertEqual(
            response.json,
            {
                'data': {
                    'type': 'F',
                    'id': '297',
                    'attributes': {
                        'other_column': None
                    },
                    'meta': {
                        'ext': ext_data
                    }
                }
            }
        )
    
    def test_extra_fields_overwrite_patch_F_200(self):
        self.add_F(
            id=90900,
            ext={
                "first": "nice",
                "second": "nicer",
                "third": "nicest",
                "fourth": "irrelevant"
            }
        )
        # overwrite 1,2 ; remove 3, leave 4 unchanged, add 5
        response = self.client.open(
            '/api/v1/F/90900',
            method='PATCH',
            json={
                'data': {
                    'type': 'F',
                    'attributes': {},
                    'meta': {
                        'ext': {
                            "first": "not very nice",
                            "second": "much less nice",
                            "third": None,
                            "fifth": "the worst of the bunch"
                        }
                    }
                }
            },
            headers=self._get_api_key()
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        expected = {
            'data': {
                'type': 'F',
                'id': '90900',
                'attributes': {
                    'other_column': None
                },
                'meta': {
                    "ext": {
                        "first": "not very nice",
                        "second": "much less nice",
                        "fourth": "irrelevant",
                        "fifth": "the worst of the bunch",
                    },
                }
            }
        }
        self.assertEqual(response.json, expected)
