# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import SpeciesService
from main.swagger import SpeciesSwagger

from .base import BaseResource, setup_resource


api_species = SpeciesSwagger.api


@setup_resource
class SpeciesResource(BaseResource):
    class Meta:
        service = SpeciesService
        swagger = SpeciesSwagger
