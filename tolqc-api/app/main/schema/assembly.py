# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcAssembly

from .base import BaseSchema, setup_schema


@setup_schema
class AssemblySchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcAssembly
