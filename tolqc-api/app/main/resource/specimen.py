# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import SpecimenService
from main.swagger import SpecimenSwagger

from tol.api_base.resource import AutoResourceGroup, setup_resource_group


api_specimen = SpecimenSwagger.api


@setup_resource_group
class SpecimenResourceGroup(AutoResourceGroup):
    class Meta:
        service = SpecimenService
        swagger = SpecimenSwagger
