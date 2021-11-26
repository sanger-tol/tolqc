# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import BaseSchema
from main.model import TolqcRun


class TolqcRunSchema(BaseSchema):
    class Meta:
        type_ = 'runs'
        strict = True
        model = TolqcRun
        include_fk = True
