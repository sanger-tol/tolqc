# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcMilestoneDict
from main.schema import MilestoneDictSchema

from tol.api_base.service import BaseService, setup_service


@setup_service
class MilestoneDictService(BaseService):
    class Meta:
        model = TolqcMilestoneDict
        schema = MilestoneDictSchema
