# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import AssemblyComponent
from main.schema import AssemblyComponentSchema

from tol.api_base.service import BaseService, setup_service


@setup_service
class AssemblyComponentService(BaseService):
    class Meta:
        model = AssemblyComponent
        schema = AssemblyComponentSchema
