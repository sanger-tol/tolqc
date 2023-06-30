# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import AssemblyComponentType

from tol.api_base.schema import BaseSchema, Str, setup_schema


@setup_schema
class AssemblyComponentTypeSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = AssemblyComponentType

    id = Str(attribute='component_type_id', dump_only=True)  # noqa: A003
