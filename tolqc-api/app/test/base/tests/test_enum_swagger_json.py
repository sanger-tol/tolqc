# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

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
        assert '/I' in paths
        assert '/I/name/{name}' in paths
        assert '/I/{id}' in paths
