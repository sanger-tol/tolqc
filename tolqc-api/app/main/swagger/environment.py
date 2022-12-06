# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask_restx import Namespace, fields


class EnvironmentSwagger:
    api = Namespace(
        'environments',
        description='Deployment environment related methods',
    )

    response_model = api.model('Environment', {
        'environment': fields.String('dev', required=True),
    })
