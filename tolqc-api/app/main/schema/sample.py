# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcSample

from .base import BaseSchema, setup_schema


@setup_schema
class SampleSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcSample
