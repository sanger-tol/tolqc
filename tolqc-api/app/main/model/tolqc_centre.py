# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from .base import Base, db


#REEEMOVE
from .base import ExtColumn


class TolqcCentre(Base):
    __tablename__ = "centre"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    hierarchy_name = db.Column(db.String(), nullable=False)
    run = db.relationship("TolqcRun", back_populates="centre")
    ext = ExtColumn()
