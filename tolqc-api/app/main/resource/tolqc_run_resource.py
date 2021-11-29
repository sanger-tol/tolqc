# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask_restx import Resource

from .base import BaseNamespace


run_namespace = BaseNamespace(
    'run',
    description='ToLQC-Run related methods',
    validate=True,
)


class TolqcRunDetailResource(Resource):
    name = "run"


class TolqcRunListResource(Resource):
    name = "runs"


run_namespace.add_resource(TolqcRunDetailResource, '/<int:id>')
run_namespace.add_resource(TolqcRunListResource, '')
