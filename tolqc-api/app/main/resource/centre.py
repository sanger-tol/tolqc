# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import CentreService
from main.swagger import CentreSwagger

from .base import AutoResourceGroup, setup_resource


api_centre = CentreSwagger.api


@setup_resource
class CentreResource(AutoResourceGroup):
    class Meta:
        service = CentreService
        swagger = CentreSwagger
