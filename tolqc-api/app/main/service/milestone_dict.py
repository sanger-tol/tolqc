# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcMilestoneDict
from main.schema import MilestoneDictSchema

from .base import BaseService, setup_service


@setup_service
class MilestoneDictService(BaseService):
    class Meta:
        model = TolqcMilestoneDict
        schema = MilestoneDictSchema
