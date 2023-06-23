# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import Dataset
from tol.api_base.schema import BaseSchema, Str, setup_schema


@setup_schema
class DatasetSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = Dataset

    id = Str(attribute='dataset_id', dump_only=True)  # noqa: A003
