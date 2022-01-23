# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcSex

from .base import BaseSchema, setup_schema


@setup_schema
class SexSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcSex
