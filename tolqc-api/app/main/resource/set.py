# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import SetService
from main.swagger import SetSwagger

from .base import BaseResource, setup_resource


api_set = SetSwagger.api


@setup_resource
class SetResource(BaseResource):
    class Meta:
        service = SetService
        swagger = SetSwagger
