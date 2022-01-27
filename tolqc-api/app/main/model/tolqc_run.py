# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .creation_log_base import CreationLogBase, db


class TolqcRun(CreationLogBase):
    __tablename__ = "run"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    hierarchy_name = db.Column(db.String())
    platform_id = db.Column(db.Integer(), db.ForeignKey("platforms.id"))
    centre_id = db.Column(db.Integer(), db.ForeignKey("centres.id"))
    lims_id = db.Column(db.Integer())
    element = db.Column(db.String())
    instrument_name = db.Column(db.String())
    seq = db.relationship("TolqcSeq", back_populates="run")
    platforms = db.relationship("TolqcPlatform", back_populates="run",
                                foreign_keys=[platform_id])
    centres = db.relationship("TolqcCentre", back_populates="run",
                              foreign_keys=[centre_id])
    pacbio_run_metrics = db.relationship("TolqcPacbioRunMetrics", back_populates="run")
