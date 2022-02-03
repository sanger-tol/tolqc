# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import AccessionTypeService
from main.swagger import AccessionTypeSwagger

from .base import BaseResource, setup_resource


api_accession_type = AccessionTypeSwagger.api


@setup_resource
class AccessionTypeResource(BaseResource):
    class Meta:
        service = AccessionTypeService
        swagger = AccessionTypeSwagger
