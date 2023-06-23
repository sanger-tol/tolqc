# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import Allocation
from main.schema import AllocationSchema
from tol.api_base.service import BaseService, setup_service


@setup_service
class AllocationService(BaseService):
    class Meta:
        model = Allocation
        schema = AllocationSchema
