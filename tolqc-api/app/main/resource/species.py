# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import SpeciesService
from main.swagger import SpeciesSwagger

from .base import BaseListResource, BaseDetailResource, setup_resource


api_species = SpeciesSwagger.api


class SpeciesResourceMeta:
    service = SpeciesService
    swagger = SpeciesSwagger


@setup_resource
class SpeciesDetailResource(BaseDetailResource):
    Meta = SpeciesResourceMeta


@setup_resource
class SpeciesListResource(BaseListResource):
    Meta = SpeciesResourceMeta
