# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import Data

from tol.api_base.schema import BaseSchema, Str, setup_schema


@setup_schema
class DataSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = Data

    id = Str(attribute='data_id', dump_only=True)  # noqa: A003
