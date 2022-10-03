# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcFile

from .base import BaseSchema, setup_schema


@setup_schema
class FileSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcFile
