# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.service import AssemblyStatusTypeService
from main.swagger import AssemblyStatusTypeSwagger
from tol.api_base.resource import AutoResourceGroup, setup_resource_group


api_assembly_status_type = AssemblyStatusTypeSwagger.api


@setup_resource_group
class AssemblyStatusTypeResourceGroup(AutoResourceGroup):
    class Meta:
        service = AssemblyStatusTypeService
        swagger = AssemblyStatusTypeSwagger
