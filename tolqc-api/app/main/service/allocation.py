# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcAllocation
from main.schema import AllocationSchema

from .base import BaseService, setup_service


@setup_service
class AllocationService(BaseService):
    class Meta:
        model = TolqcAllocation
        schema = AllocationSchema
