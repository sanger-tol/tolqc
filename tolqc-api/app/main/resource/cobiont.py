# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import CobiontService
from main.swagger import CobiontSwagger

from .base import BaseResource, setup_resource


api_cobiont = CobiontSwagger.api


@setup_resource
class CobiontResource(BaseResource):
    class Meta:
        service = CobiontService
        swagger = CobiontSwagger
