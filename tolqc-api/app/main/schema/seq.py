# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcSeq

from .base import BaseSchema, setup_schema


@setup_schema
class SeqSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcSeq
