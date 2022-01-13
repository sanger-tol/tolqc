# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcLibraryType

from .base import BaseSchema, setup_schema


@setup_schema
class LibraryTypeSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcLibraryType
