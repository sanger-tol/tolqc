# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import RunService
from main.swagger import RunSwagger

from .base import BaseResource, setup_resource


api_run = RunSwagger.api


@setup_resource
class RunResource(BaseResource):
    class Meta:
        service = RunService
        swagger = RunSwagger
