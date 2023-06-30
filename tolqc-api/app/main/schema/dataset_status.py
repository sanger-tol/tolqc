# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import DatasetStatus

from tol.api_base.schema import BaseSchema, Str, setup_schema


@setup_schema
class DatasetStatusSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = DatasetStatus

    id = Str(attribute='dataset_status_id', dump_only=True)  # noqa: A003
