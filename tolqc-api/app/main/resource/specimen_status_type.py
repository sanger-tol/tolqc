# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.service import SpecimenStatusTypeService
from main.swagger import SpecimenStatusTypeSwagger

from tol.api_base.resource import AutoResourceGroup, setup_resource_group


api_specimen_status_type = SpecimenStatusTypeSwagger.api


@setup_resource_group
class SpecimenStatusTypeResourceGroup(AutoResourceGroup):
    class Meta:
        service = SpecimenStatusTypeService
        swagger = SpecimenStatusTypeSwagger
