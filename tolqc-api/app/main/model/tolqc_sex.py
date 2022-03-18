# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import db, EnumBase, setup_model


@setup_model
class TolqcSex(EnumBase):
    __tablename__ = "sex"

    class Meta:
        type_ = 'sexes'

    specimen = db.relationship("TolqcSpecimen", back_populates="sex")
