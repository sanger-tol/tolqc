# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import BaseDetailRequestSchema, BaseDetailResponseSchema
from main.model import TolqcCentre


class TolqcCentreRequestSchema(BaseDetailRequestSchema):
    class Meta:
        type_ = 'centre'
        strict = True
        model = TolqcCentre
        include_fk = True


class TolqcCentreResponseSchema(BaseDetailResponseSchema):
    class Meta:
        type_ = 'centre'
        strict = True
        model = TolqcCentre
        include_fk = True
