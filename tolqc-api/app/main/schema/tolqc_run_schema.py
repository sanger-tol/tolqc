# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model.tolqc_run import TolqcRun
from main.ma import ma


class TolqcRunSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TolqcRun
        load_instance = True
        include_fk = True
