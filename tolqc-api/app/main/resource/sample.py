# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import SampleService
from main.swagger import SampleSwagger

from .base import BaseListResource, BaseDetailResource, setup_resource


api_sample = SampleSwagger.api


class SampleResourceMeta:
    service = SampleService
    swagger = SampleSwagger


@setup_resource
class SampleDetailResource(BaseDetailResource):
    Meta = SampleResourceMeta


@setup_resource
class SampleListResource(BaseListResource):
    Meta = SampleResourceMeta
