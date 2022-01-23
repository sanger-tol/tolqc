# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcAsm
from main.schema import AsmSchema

from .base import BaseService


class AsmService(BaseService):
    class Meta:
        model = TolqcAsm
        schema = AsmSchema
