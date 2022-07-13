# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import AssemblyComponentService
from main.swagger import AssemblyComponentSwagger

from .base import AutoResourceGroup, setup_resource


api_assembly_component = AssemblyComponentSwagger.api


@setup_resource
class AssemblyComponentResource(AutoResourceGroup):
    class Meta:
        service = AssemblyComponentService
        swagger = AssemblyComponentSwagger
