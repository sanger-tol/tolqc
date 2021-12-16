# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask_restx import fields, Namespace


class EnvironmentSwagger:
    api = Namespace(
        'environments',
        description='Deployment environment related methods',
    )

    response_model = api.model('Environment', {
        'environment': fields.String("dev", required=True),
    })
