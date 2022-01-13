# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import SpecimenService
from main.swagger import SpecimenSwagger

from .base import BaseListResource, BaseDetailResource, setup_resource


api_specimen = SpecimenSwagger.api


class SpecimenResourceMeta:
    service = SpecimenService
    swagger = SpecimenSwagger


@setup_resource
class SpecimenDetailResource(BaseDetailResource):
    Meta = SpecimenResourceMeta


@setup_resource
class SpecimenListResource(BaseListResource):
    Meta = SpecimenResourceMeta
