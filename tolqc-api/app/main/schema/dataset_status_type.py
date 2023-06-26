# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import DatasetStatusType

from tol.api_base.schema import BaseSchema, Str, setup_schema


@setup_schema
class DatasetStatusTypeSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = DatasetStatusType

    id = Str(attribute='status_type_id', dump_only=True)  # noqa: A003
