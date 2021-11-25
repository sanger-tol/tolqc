# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask_restx import Namespace

from .base import BaseDetailResource, BaseListResource
from main.schema import TolqcRunSchema


run_namespace = Namespace(
    'run',
    description='ToLQC-Run related methods',
)


class TolqcRunDetailResource(BaseDetailResource):
    allowed_methods = ['get']
    name = "run"
    schema = TolqcRunSchema()


class TolqcRunListResource(BaseListResource):
    name = "runs"
    schema = TolqcRunSchema()


run_namespace.add_resource(TolqcRunDetailResource, '/<int:id>')
run_namespace.add_resource(TolqcRunListResource, '')
