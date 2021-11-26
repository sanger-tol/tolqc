# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import BaseRequestSchema, BaseResponseSchema
from main.model import TolqcCentre


class TolqcCentreRequestSchema(BaseRequestSchema):
    class Meta:
        type_ = 'centre'
        strict = True
        model = TolqcCentre


class TolqcCentreResponseSchema(BaseResponseSchema):
    class Meta:
        type_ = 'centre'
        strict = True
        model = TolqcCentre
        include_fk = True
