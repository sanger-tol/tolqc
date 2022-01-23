# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcSeqData
from main.schema import SeqDataSchema

from .base import BaseService


class SeqDataService(BaseService):
    class Meta:
        model = TolqcSeqData
        schema = SeqDataSchema
