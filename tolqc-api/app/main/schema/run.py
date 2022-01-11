# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcRun

from .base import BaseSchema, setup_schema


@setup_schema
class RunSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcRun
