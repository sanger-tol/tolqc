# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcAsm

from .base import BaseSchema, setup_schema


@setup_schema
class AsmSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcAsm
