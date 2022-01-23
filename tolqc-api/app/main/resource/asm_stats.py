# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import AsmStatsService
from main.swagger import AsmStatsSwagger

from .base import BaseListResource, BaseDetailResource, setup_resource


api_asm_stats = AsmStatsSwagger.api


class AsmStatsResourceMeta:
    service = AsmStatsService
    swagger = AsmStatsSwagger


@setup_resource
class AsmStatsDetailResource(BaseDetailResource):
    Meta = AsmStatsResourceMeta


@setup_resource
class AsmStatsListResource(BaseListResource):
    Meta = AsmStatsResourceMeta
