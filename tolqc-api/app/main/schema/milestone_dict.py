# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcMilestoneDict

from .base import BaseSchema, setup_schema


@setup_schema
class MilestoneDictSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcMilestoneDict
