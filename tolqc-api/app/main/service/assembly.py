# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcAssembly
from main.schema import AssemblySchema

from .base import BaseService, setup_service


@setup_service
class AssemblyService(BaseService):
    class Meta:
        model = TolqcAssembly
        schema = AssemblySchema
