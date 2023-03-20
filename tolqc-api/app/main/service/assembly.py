# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import Assembly
from main.schema import AssemblySchema

from tol.api_base.service import BaseService, setup_service


@setup_service
class AssemblyService(BaseService):
    class Meta:
        model = Assembly
        schema = AssemblySchema
