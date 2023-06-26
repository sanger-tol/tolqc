# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import AssemblySource
from main.schema import AssemblySourceSchema

from tol.api_base.service import BaseService, setup_service


@setup_service
class AssemblySourceService(BaseService):
    class Meta:
        model = AssemblySource
        schema = AssemblySourceSchema
