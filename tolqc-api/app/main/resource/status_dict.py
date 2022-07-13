# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import StatusDictService
from main.swagger import StatusDictSwagger

from .base import AutoResourceGroup, setup_resource


api_status_dict = StatusDictSwagger.api


@setup_resource
class StatusDictResource(AutoResourceGroup):
    class Meta:
        service = StatusDictService
        swagger = StatusDictSwagger
