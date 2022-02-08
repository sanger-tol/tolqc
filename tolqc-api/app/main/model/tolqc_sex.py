# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import db, setup_model
from .enum_base import EnumBase


@setup_model
class TolqcSex(EnumBase):
    __tablename__ = "sex"
    specimen = db.relationship("TolqcSpecimen", back_populates="sex")
