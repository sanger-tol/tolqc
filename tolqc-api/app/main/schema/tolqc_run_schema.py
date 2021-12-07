# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import BaseDetailRequestSchema, BaseDetailResponseSchema
from main.model import TolqcRun


class TolqcRunRequestSchema(BaseDetailRequestSchema):
    class Meta:
        type_ = 'run'
        strict = True
        model = TolqcRun
        include_fk = True


class TolqcRunResponseSchema(BaseDetailResponseSchema):
    class Meta:
        type_ = 'run'
        strict = True
        model = TolqcRun
        include_fk = True
