# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcAsmStats
from main.schema import AsmStatsSchema

from .base import BaseService


class AsmStatsService(BaseService):
    class Meta:
        model = TolqcAsmStats
        schema = AsmStatsSchema
