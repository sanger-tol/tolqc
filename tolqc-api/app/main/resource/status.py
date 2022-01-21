# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import StatusService
from main.swagger import StatusSwagger

from .base import BaseListResource, BaseDetailResource, setup_resource


api_Status = StatusSwagger.api


class StatusResourceMeta:
    service = StatusService
    swagger = StatusSwagger


@setup_resource
class StatusDetailResource(BaseDetailResource):
    Meta = StatusResourceMeta


@setup_resource
class StatusListResource(BaseListResource):
    Meta = StatusResourceMeta
