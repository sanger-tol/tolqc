# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import Sex

from tol.api_base.schema import BaseSchema, Str, setup_schema


@setup_schema
class SexSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = Sex

    id = Str(attribute='sex_id', dump_only=True)  # noqa: A003
