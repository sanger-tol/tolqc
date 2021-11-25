# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import BaseDetailResource, BaseListResource, BaseNamespace
from main.schema import TolqcRunSchema


run_namespace = BaseNamespace(
    'run',
    description='ToLQC-Run related methods',
)


class TolqcRunDetailResource(BaseDetailResource):
    namespace = run_namespace
    allowed_methods = ['get']
    name = "run"
    schema = TolqcRunSchema()


class TolqcRunListResource(BaseListResource):
    namespace = run_namespace
    name = "runs"
    schema = TolqcRunSchema()


run_namespace.add_resource(TolqcRunDetailResource, '/<int:id>')
run_namespace.add_resource(TolqcRunListResource, '')
