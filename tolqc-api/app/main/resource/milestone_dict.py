# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import MilestoneDictService
from main.swagger import MilestoneDictSwagger

from .base import AutoResourceGroup, setup_resource_group


api_milestone_dict = MilestoneDictSwagger.api


@setup_resource_group
class MilestoneDictResourceGroup(AutoResourceGroup):
    class Meta:
        service = MilestoneDictService
        swagger = MilestoneDictSwagger
