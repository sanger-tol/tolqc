# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import AssemblyComponentService
from main.swagger import AssemblyComponentSwagger

from .tol.api_base.resource import AutoResourceGroup, setup_resource_group


api_assembly_component = AssemblyComponentSwagger.api


@setup_resource_group
class AssemblyComponentResourceGroup(AutoResourceGroup):
    class Meta:
        service = AssemblyComponentService
        swagger = AssemblyComponentSwagger
