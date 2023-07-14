# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import Run

from tol.api_base.schema import BaseSchema, Str, setup_schema


@setup_schema
class RunSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = Run

    id = Str(attribute='run_id', dump_only=True)  # noqa: A003
