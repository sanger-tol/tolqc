# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import BaseRequestSchema, BaseResponseSchema
from main.model import TolqcRun


class TolqcRunRequestSchema(BaseRequestSchema):
    class Meta:
        type_ = 'run'
        strict = True
        model = TolqcRun
        include_fk = True


class TolqcRunResponseSchema(BaseResponseSchema):
    class Meta:
        type_ = 'run'
        strict = True
        model = TolqcRun
        include_fk = True
