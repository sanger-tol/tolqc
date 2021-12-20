# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.constant import Types
from main.model import TolqcCentre

from .base import BaseSchema, BaseMeta, setup_schema


@setup_schema
class CentreSchema(BaseSchema):
    class Meta(BaseMeta):
        model = TolqcCentre
        type_ = Types.CENTRE
