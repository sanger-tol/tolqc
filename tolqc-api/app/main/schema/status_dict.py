# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcStatusDict

from .base import BaseSchema, setup_schema


@setup_schema
class StatusDictSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcStatusDict
