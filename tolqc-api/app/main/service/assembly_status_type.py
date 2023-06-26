# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import AssemblyStatusType
from main.schema import AssemblyStatusTypeSchema

from tol.api_base.service import BaseService, setup_service


@setup_service
class AssemblyStatusTypeService(BaseService):
    class Meta:
        model = AssemblyStatusType
        schema = AssemblyStatusTypeSchema
