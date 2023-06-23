# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import AssemblySource
from tol.api_base.schema import BaseSchema, setup_schema


@setup_schema
class AssemblySourceSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = AssemblySource
