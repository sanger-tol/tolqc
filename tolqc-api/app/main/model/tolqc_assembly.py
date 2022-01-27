# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .creation_log_base import CreationLogBase, db


class TolqcAssembly(CreationLogBase):
    __tablename__ = "assembly"
    id = db.Column(db.Integer(), primary_key=True)
    data_id = db.Column(db.Integer(), db.ForeignKey("data.id"))
    name = db.Column(db.String())
    description = db.Column(db.String())
    data = db.relationship("TolqcData", back_populates="assembly",
                           foreign_keys=[data_id])
    assembly_metrics = db.relationship("TolqcAssemblyMetrics", back_populates="assembly")
    busco_metrics = db.relationship("TolqcBuscoMetrics", back_populates="assembly")
    merqury_metrics = db.relationship("TolqcMerquryMetrics", back_populates="assembly")
