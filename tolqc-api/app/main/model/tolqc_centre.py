# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db
from .base import setup_model


@setup_model
class TolqcCentre(Base):
    __tablename__ = "centre"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    hierarchy_name = db.Column(db.String())
    run = db.relationship("TolqcRun", back_populates="centre")
