# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from urllib.parse import unquote_plus

from test.base import BaseTestCase


class TestEnumSwaggerJson(BaseTestCase):
    def _get_swagger_json_file(self):
        response = self.client.open(
            '/api/v1/swagger.json',
            method='GET'
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
        return response.json

    def test_all_enum_paths_in_swagger(self):
        swagger_json = self._get_swagger_json_file()
        paths = list(swagger_json['paths'].keys())

        # assert that all I (enum) paths (including name) are in there
        assert '/enum/I' in paths
        assert '/enum/I/{name}' in paths
        assert '/enum/I/{name}/J' in paths

        # assert that other (non-enum) endpoints do not have name paths
        assert '/B/{name}' not in paths
        assert '/B/{name}/E' not in paths
        assert '/enum/B/{name}' not in paths
        assert '/enum/B/{name}/E' not in paths

    def _get_response_model(self, swagger_json, method, path, code):
        method_dict = swagger_json['paths'][path][method]
        response_ref = method_dict['responses'][code]['schema']['$ref']
        response_model_name = unquote_plus(response_ref.split('/')[2])
        return swagger_json['definitions'][response_model_name]

    def test_enum_by_name_response_models_same_as_by_id_detail_get(self):
        swagger_json = self._get_swagger_json_file()

        response_model_by_name = self._get_response_model(
            swagger_json,
            'get',
            '/I/name/{name}',
            '200'
        )
        response_model_by_id = self._get_response_model(
            swagger_json,
            'get',
            '/I/{id}',
            '200'
        )

        self.assertEqual(response_model_by_id, response_model_by_name)

    def test_enum_by_name_response_models_same_as_by_id_detail_patch(self):
        swagger_json = self._get_swagger_json_file()

        response_model_by_name = self._get_response_model(
            swagger_json,
            'patch',
            '/I/name/{name}',
            '200'
        )
        response_model_by_id = self._get_response_model(
            swagger_json,
            'patch',
            '/I/{id}',
            '200'
        )

        self.assertEqual(response_model_by_id, response_model_by_name)

    def test_enum_by_name_response_models_same_as_by_id_relation_list_get(self):
        swagger_json = self._get_swagger_json_file()

        response_model_by_name = self._get_response_model(
            swagger_json,
            'get',
            '/I/name/{name}/J',
            '200'
        )
        response_model_by_id = self._get_response_model(
            swagger_json,
            'get',
            '/I/{id}/J',
            '200'
        )

        self.assertEqual(response_model_by_id, response_model_by_name)
