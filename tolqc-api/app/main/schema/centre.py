# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcCentre

from .base import BaseSchema


class CentreSchema(BaseSchema):
    class Meta:
        model = TolqcCentre
