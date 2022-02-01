# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .log_base import LogBase, db
from .base import setup_model


@setup_model
class TolqcAssembly(LogBase):
    __tablename__ = "assembly"
    id = db.Column(db.Integer(), primary_key=True)
    dataset_id = db.Column(db.Integer(), db.ForeignKey("dataset.id"))
    name = db.Column(db.String())
    description = db.Column(db.String())
    dataset = db.relationship("TolqcDataset", back_populates="assembly",
                              foreign_keys=[dataset_id])
    assembly_metrics = db.relationship("TolqcAssemblyMetrics", back_populates="assembly")
    busco_metrics = db.relationship("TolqcBuscoMetrics", back_populates="assembly")
    merqury_metrics = db.relationship("TolqcMerquryMetrics", back_populates="assembly")
