# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db


class TolqcRun(Base):
    __tablename__ = "run"
    row_id = db.Column(db.Integer())
    run_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    hierarchy_name = db.Column(db.String())
    platform_id = db.Column(db.Integer(), db.ForeignKey("platform.platform_id"))
    centre_id = db.Column(db.Integer(), db.ForeignKey("centre.centre_id"))
    lims_id = db.Column(db.Integer())
    element = db.Column(db.String())
    changed = db.Column(db.DateTime())
    current = db.Column(db.DateTime())
    seq = db.relationship("TolqcSeq", back_populates="run")
    platform = db.relationship("TolqcPlatform", back_populates="run")
    centre = db.relationship("TolqcCentre", back_populates="run")
