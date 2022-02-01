# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db, setup_model


@setup_model
class TolqcMilestoneDict(Base):
    __tablename__ = "milestone_dict"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String())
    status = db.relationship("TolqcStatus", back_populates="milestone_dict")
