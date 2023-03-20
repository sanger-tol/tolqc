# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import AssemblyComponent

from tol.api_base.schema import BaseSchema, setup_schema


@setup_schema
class AssemblyComponentSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = AssemblyComponent
