# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import MilestoneDictService
from main.swagger import MilestoneDictSwagger

from .base import AutoResourceGroup, setup_resource


api_milestone_dict = MilestoneDictSwagger.api


@setup_resource
class MilestoneDictResource(AutoResourceGroup):
    class Meta:
        service = MilestoneDictService
        swagger = MilestoneDictSwagger
