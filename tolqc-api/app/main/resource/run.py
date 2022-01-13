# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import RunService
from main.swagger import RunSwagger

from .base import BaseListResource, BaseDetailResource, setup_resource


api_run = RunSwagger.api


class RunResourceMeta:
    service = RunService
    swagger = RunSwagger


@setup_resource
class RunDetailResource(BaseDetailResource):
    Meta = RunResourceMeta


@setup_resource
class RunListResource(BaseListResource):
    Meta = RunResourceMeta
