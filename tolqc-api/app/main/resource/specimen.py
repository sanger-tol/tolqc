# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import SpecimenService
from main.swagger import SpecimenSwagger

from .base import BaseResource, setup_resource


api_specimen = SpecimenSwagger.api


@setup_resource
class SpecimenResource(BaseResource):
    class Meta:
        service = SpecimenService
        swagger = SpecimenSwagger
