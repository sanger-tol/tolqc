# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import AssemblyComponentType
from main.schema import AssemblyComponentTypeSchema
from tol.api_base.service import BaseService, setup_service


@setup_service
class AssemblyComponentTypeService(BaseService):
    class Meta:
        model = AssemblyComponentType
        schema = AssemblyComponentTypeSchema
