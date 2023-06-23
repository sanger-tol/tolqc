# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import Sample
from tol.api_base.schema import BaseSchema, Str, setup_schema


@setup_schema
class SampleSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = Sample

    id = Str(attribute='sample_id', dump_only=True)  # noqa: A003
