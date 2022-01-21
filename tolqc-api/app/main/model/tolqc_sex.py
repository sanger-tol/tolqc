# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db


class TolqcSex(Base):
    __tablename__ = "sex"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    specimens = db.relationship("TolqcSpecimen", back_populates="sex")
