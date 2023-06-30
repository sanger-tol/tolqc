# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.service import AssemblySourceService
from main.swagger import AssemblySourceSwagger

from tol.api_base.resource import AutoResourceGroup, setup_resource_group


api_assembly_source = AssemblySourceSwagger.api


@setup_resource_group
class AssemblySourceResourceGroup(AutoResourceGroup):
    class Meta:
        service = AssemblySourceService
        swagger = AssemblySourceSwagger
