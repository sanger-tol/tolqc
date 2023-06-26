# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import AssemblyStatus
from main.schema import AssemblyStatusSchema

from tol.api_base.service import BaseService, setup_service


@setup_service
class AssemblyStatusService(BaseService):
    class Meta:
        model = AssemblyStatus
        schema = AssemblyStatusSchema
