# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db, LogMixin, setup_model


@setup_model
class TolqcRun(LogMixin, Base):
    __tablename__ = "run"

    class Meta:
        type_ = 'runs'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    hierarchy_name = db.Column(db.String())
    platform_id = db.Column(db.Integer(), db.ForeignKey("platform.id"))
    centre_id = db.Column(db.Integer(), db.ForeignKey("centre.id"))
    lims_id = db.Column(db.Integer())
    element = db.Column(db.String())
    instrument_name = db.Column(db.String())
    data = db.relationship("TolqcData", back_populates="run")
    platform = db.relationship("TolqcPlatform", back_populates="run",
                               foreign_keys=[platform_id])
    centre = db.relationship("TolqcCentre", back_populates="run",
                             foreign_keys=[centre_id])
    pacbio_run_metrics = db.relationship("TolqcPacbioRunMetrics", back_populates="run")
