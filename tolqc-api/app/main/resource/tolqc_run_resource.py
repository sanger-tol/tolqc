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


class TolqcRunResource(BaseDetailResource):
    name = "run"
    schema = TolqcRunSchema()


class TolqcRunListResource(BaseListResource):
    name = "runs"
    schema = TolqcRunSchema()
