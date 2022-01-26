# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import PacbioRunStatsService
from main.swagger import PacbioRunStatsSwagger

from .base import BaseResource, setup_resource


api_pacbio_run_stats = PacbioRunStatsSwagger.api


@setup_resource
class PacbioRunStatsResource(BaseResource):
    class Meta:
        service = PacbioRunStatsService
        swagger = PacbioRunStatsSwagger
