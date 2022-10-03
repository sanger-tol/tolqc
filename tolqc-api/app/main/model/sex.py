# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import db, setup_model
from .enum_base import EnumBase


@setup_model
class TolqcSex(EnumBase):
    __tablename__ = "sex"

    class Meta:
        type_ = 'sexes'

    specimen = db.relationship("TolqcSpecimen", back_populates="sex")
