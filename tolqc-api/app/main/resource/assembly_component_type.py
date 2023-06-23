# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.service import AssemblyComponentTypeService
from main.swagger import AssemblyComponentTypeSwagger
from tol.api_base.resource import AutoResourceGroup, setup_resource_group


api_assembly_component_type = AssemblyComponentTypeSwagger.api


@setup_resource_group
class AssemblyComponentTypeResourceGroup(AutoResourceGroup):
    class Meta:
        service = AssemblyComponentTypeService
        swagger = AssemblyComponentTypeSwagger
