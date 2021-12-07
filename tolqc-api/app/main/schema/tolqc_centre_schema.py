# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcCentre

from .base import BaseDetailRequestSchema, BaseDetailResponseSchema, \
                  BaseListRequestSchema, BaseListResponseSchema, BaseMeta


class CentreMeta(BaseMeta):
    type_ = 'centre'
    model = TolqcCentre


class CentreDetailRequestSchema(BaseDetailRequestSchema):
    Meta = CentreMeta


class CentreDetailResponseSchema(BaseDetailResponseSchema):
    Meta = CentreMeta


class CentreListRequestSchema(BaseListRequestSchema):
    Meta = CentreMeta


class CentreListResponseSchema(BaseListResponseSchema):
    Meta = CentreMeta
