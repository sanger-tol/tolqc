# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import LibraryType

from tol.api_base.schema import BaseSchema, Str, setup_schema


@setup_schema
class LibraryTypeSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = LibraryType

    id = Str(attribute='library_type_id', dump_only=True)  # noqa: A003
