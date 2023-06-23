# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import ReviewDict
from tol.api_base.schema import BaseSchema, Str, setup_schema


@setup_schema
class ReviewDictSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = ReviewDict

    id = Str(attribute='review_id', dump_only=True)  # noqa: A003
