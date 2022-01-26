# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import StatusService
from main.swagger import StatusSwagger

from .base import BaseResource, setup_resource


api_status = StatusSwagger.api


@setup_resource
class StatusResource(BaseResource):
    class Meta:
        service = StatusService
        swagger = StatusSwagger
