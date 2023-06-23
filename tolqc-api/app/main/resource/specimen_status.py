# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.service import SpecimenStatusService
from main.swagger import SpecimenStatusSwagger
from tol.api_base.resource import AutoResourceGroup, setup_resource_group


api_specimen_status = SpecimenStatusSwagger.api


@setup_resource_group
class SpecimenStatusResourceGroup(AutoResourceGroup):
    class Meta:
        service = SpecimenStatusService
        swagger = SpecimenStatusSwagger
