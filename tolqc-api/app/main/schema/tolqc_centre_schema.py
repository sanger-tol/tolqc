# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import BaseSchema
from main.model import TolqcCentre


class TolqcCentreSchema(BaseSchema):
    class Meta:
        type_ = 'centres'
        strict = True
        model = TolqcCentre
        include_fk = True
