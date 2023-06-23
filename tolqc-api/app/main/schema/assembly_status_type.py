# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import AssemblyStatusType
from tol.api_base.schema import BaseSchema, Str, setup_schema


@setup_schema
class AssemblyStatusTypeSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = AssemblyStatusType

    id = Str(attribute='status_type_id', dump_only=True)  # noqa: A003
