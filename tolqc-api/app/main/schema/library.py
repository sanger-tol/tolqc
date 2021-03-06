# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcLibrary

from .base import BaseSchema, setup_schema


@setup_schema
class LibrarySchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcLibrary
