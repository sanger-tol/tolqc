# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
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

        # assert that all I (enum) paths (including name) are in there
        assert '/enum/I' in paths
        assert '/enum/I/{name}' in paths
        assert '/enum/I/{name}/J' in paths

        # assert that other (non-enum) endpoints do not have name paths
        assert '/B/{name}' not in paths
        assert '/B/{name}/E' not in paths
        assert '/enum/B/{name}' not in paths
        assert '/enum/B/{name}/E' not in paths
