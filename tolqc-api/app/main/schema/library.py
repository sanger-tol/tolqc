# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import Library
from tol.api_base.schema import BaseSchema, Str, setup_schema


@setup_schema
class LibrarySchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = Library

    id = Str(attribute='library_id', dump_only=True)  # noqa: A003
