# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import SpecimenService
from main.swagger import SpecimenSwagger

from .base import AutoResourceGroup, setup_resource_group


api_specimen = SpecimenSwagger.api


@setup_resource_group
class SpecimenResourceGroup(AutoResourceGroup):
    class Meta:
        service = SpecimenService
        swagger = SpecimenSwagger
