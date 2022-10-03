# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import StatusDictService
from main.swagger import StatusDictSwagger

from .base import AutoResourceGroup, setup_resource_group


api_status_dict = StatusDictSwagger.api


@setup_resource_group
class StatusDictResourceGroup(AutoResourceGroup):
    class Meta:
        service = StatusDictService
        swagger = StatusDictSwagger
