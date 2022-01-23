# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcMerqury

from .base import BaseSchema, setup_schema


@setup_schema
class MerqurySchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcMerqury
