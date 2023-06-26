# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.service import AssemblyStatusService
from main.swagger import AssemblyStatusSwagger

from tol.api_base.resource import AutoResourceGroup, setup_resource_group


api_assembly_status = AssemblyStatusSwagger.api


@setup_resource_group
class AssemblyStatusResourceGroup(AutoResourceGroup):
    class Meta:
        service = AssemblyStatusService
        swagger = AssemblyStatusSwagger
