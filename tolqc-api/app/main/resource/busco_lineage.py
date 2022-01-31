# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import Busco_LineageService
from main.swagger import Busco_LineageSwagger

from .base import BaseResource, setup_resource


api_busco_lineage = Busco_LineageSwagger.api


@setup_resource
class Busco_LineageResource(BaseResource):
    class Meta:
        service = Busco_LineageService
        swagger = Busco_LineageSwagger
