# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcAllocation

from .base import BaseSchema, setup_schema


@setup_schema
class AllocationSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcAllocation
