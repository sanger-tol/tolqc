# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import SexService
from main.swagger import SexSwagger

from .base import BaseResource, setup_resource


api_sex = SexSwagger.api


@setup_resource
class SexResource(BaseResource):
    class Meta:
        service = SexService
        swagger = SexSwagger
