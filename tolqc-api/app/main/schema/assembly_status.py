# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import AssemblyStatus
from tol.api_base.schema import BaseSchema, Str, setup_schema


@setup_schema
class AssemblyStatusSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = AssemblyStatus

    id = Str(attribute='assembly_status_id', dump_only=True)  # noqa: A003
