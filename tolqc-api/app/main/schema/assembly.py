# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import Assembly

from tol.api_base.schema import BaseSchema, Str, setup_schema


@setup_schema
class AssemblySchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = Assembly

    id = Str(attribute='assembly_id', dump_only=True)  # noqa: A003
