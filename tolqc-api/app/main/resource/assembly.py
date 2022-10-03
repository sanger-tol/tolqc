# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import AssemblyService
from main.swagger import AssemblySwagger

from .base import AutoResourceGroup, setup_resource_group


api_assembly = AssemblySwagger.api


@setup_resource_group
class AssemblyResourceGroup(AutoResourceGroup):
    class Meta:
        service = AssemblyService
        swagger = AssemblySwagger
