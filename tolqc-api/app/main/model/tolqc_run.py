# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .sub_base import CreationLogBase, db


class TolqcRun(CreationLogBase):
    __tablename__ = "run"
    id = db.Column(db.Integer(), primary_key=True)
    run_id = db.Column(db.Integer(), nullable=False)
    name = db.Column(db.String(), nullable=False)
    hierarchy_name = db.Column(db.String(), nullable=False)
    platform_id = db.Column(db.Integer(), db.ForeignKey("platform.id"),
                            nullable=False)
    centre_id = db.Column(db.Integer(), db.ForeignKey("centres.id"),
                          nullable=False)
    lims_id = db.Column(db.Integer())
    element = db.Column(db.String())
    changed = db.Column(db.DateTime())
    current = db.Column(db.Boolean())
    seq = db.relationship("TolqcSeq", back_populates="run")
    platform = db.relationship("TolqcPlatform", back_populates="run", foreign_keys=[platform_id])
    centres = db.relationship("TolqcCentre", back_populates="run", foreign_keys=[centre_id])
