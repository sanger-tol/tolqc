# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import Run

from tol.api_base.schema import BaseSchema, setup_schema


@setup_schema
class RunSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = Run
