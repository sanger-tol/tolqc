# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import PacbioRunStatsService
from main.swagger import PacbioRunStatsSwagger

from .base import BaseListResource, BaseDetailResource, setup_resource


api_pacbio_run_stats = PacbioRunStatsSwagger.api


class PacbioRunStatsResourceMeta:
    service = PacbioRunStatsService
    swagger = PacbioRunStatsSwagger


@setup_resource
class PacbioRunStatsDetailResource(BaseDetailResource):
    Meta = PacbioRunStatsResourceMeta


@setup_resource
class PacbioRunStatsListResource(BaseListResource):
    Meta = PacbioRunStatsResourceMeta
