# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import Assembly

from tol.api_base.schema import BaseSchema, setup_schema


@setup_schema
class AssemblySchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = Assembly
