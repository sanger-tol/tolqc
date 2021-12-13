# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcRun
from .base import BaseMeta, BaseDetailSchema, BaseListSchema


class RunMeta(BaseMeta):
    type_ = 'run'
    model = TolqcRun


class RunDetailSchema(BaseDetailSchema):
    Meta = RunMeta


class RunListSchema(BaseListSchema):
    Meta = RunMeta
