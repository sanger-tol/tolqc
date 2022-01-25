# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import AsmStatsService
from main.swagger import AsmStatsSwagger

from .base import BaseResource, setup_resource


api_asm_stats = AsmStatsSwagger.api


@setup_resource
class AsmStatsResource(BaseResource):
    class Meta:
        service = AsmStatsService
        swagger = AsmStatsSwagger
