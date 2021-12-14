# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcCentre

from .base import BaseDetailSchema, BaseListSchema, BaseMeta


class CentreMeta(BaseMeta):
    type_ = 'centre'
    model = TolqcCentre


class CentreDetailSchema(BaseDetailSchema):
    Meta = CentreMeta


class CentreListSchema(BaseListSchema):
    Meta = CentreMeta