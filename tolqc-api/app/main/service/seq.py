# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcSeq
from main.schema import SeqSchema

from .base import BaseService


class SeqService(BaseService):
    class Meta:
        model = TolqcSeq
        schema = SeqSchema
