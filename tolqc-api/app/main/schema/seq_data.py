# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcSeqData

from .base import BaseSchema, setup_schema


@setup_schema
class SeqDataSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcSeqData
