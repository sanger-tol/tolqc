# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import SpeciesService
from main.swagger import SpeciesSwagger

from tol.api_base.resource import AutoResourceGroup, setup_resource_group


api_species = SpeciesSwagger.api


@setup_resource_group
class SpeciesResourceGroup(AutoResourceGroup):
    class Meta:
        service = SpeciesService
        swagger = SpeciesSwagger
