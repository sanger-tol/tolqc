# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcAllocation
from main.schema import AllocationSchema

from .base import BaseService


class AllocationService(BaseService):
    class Meta:
        model = TolqcAllocation
        schema = AllocationSchema
