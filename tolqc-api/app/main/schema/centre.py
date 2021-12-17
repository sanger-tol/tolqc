# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.constant import Types
from main.model import TolqcCentre

from .base import BaseSchema, BaseMeta, setup_schema, BaseExtMeta, BaseExtSchema


@setup_schema
class CentreSchema(BaseExtSchema): #CHANGE THIS BACK!!!!
    class Meta(BaseExtMeta):
        model = TolqcCentre
        type_ = Types.CENTRE
