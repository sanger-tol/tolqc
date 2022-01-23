# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcData

from .base import BaseSchema, setup_schema


@setup_schema
class DataSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcData
