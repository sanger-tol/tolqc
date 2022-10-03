# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcSet

from .base import BaseSchema, setup_schema


@setup_schema
class SetSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcSet
