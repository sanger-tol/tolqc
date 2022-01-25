# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import AsmService
from main.swagger import AsmSwagger

from .base import BaseResource, setup_resource


api_asm = AsmSwagger.api


@setup_resource
class AsmResource(BaseResource):
    class Meta:
        service = AsmService
        swagger = AsmSwagger
