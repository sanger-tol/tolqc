# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcPacbioRunStats
from main.schema import PacbioRunStatsSchema

from .base import BaseService, setup_service


@setup_service
class PacbioRunStatsService(BaseService):
    class Meta:
        model = TolqcPacbioRunStats
        schema = PacbioRunStatsSchema
