# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import StatusService
from main.swagger import StatusSwagger

from .base import AutoResourceGroup, setup_resource_group


api_status = StatusSwagger.api


@setup_resource_group
class StatusResourceGroup(AutoResourceGroup):
    class Meta:
        service = StatusService
        swagger = StatusSwagger
