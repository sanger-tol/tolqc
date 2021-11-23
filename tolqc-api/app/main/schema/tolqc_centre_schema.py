# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.ma import ma
from .base import BaseSchema
from main.model.tolqc_centre import TolqcCentre
from main.model.tolqc_run import TolqcRun


class TolqcCentreSchema(BaseSchema):
    runs = ma.Nested(TolqcRun, many=True)

    class Meta:
        model = TolqcCentre
        load_instance = True
        include_fk = True
        type_ = 'centre'
        id = 'centre_id'
