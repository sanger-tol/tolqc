# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcQcDict

from .base import BaseSchema, setup_schema


@setup_schema
class QcDictSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcQcDict
