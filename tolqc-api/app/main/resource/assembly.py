# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import AssemblyService
from main.swagger import AssemblySwagger

from .base import BaseResource, setup_resource


api_assembly = AssemblySwagger.api


@setup_resource
class AssemblyResource(BaseResource):
    class Meta:
        service = AssemblyService
        swagger = AssemblySwagger
