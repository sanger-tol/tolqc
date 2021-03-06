# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .log_base import LogBase, db
from .base import setup_model


@setup_model
class TolqcMerquryMetrics(LogBase):
    __tablename__ = "merqury_metrics"

    class Meta:
        type_ = 'merqury_metrics'

    id = db.Column(db.Integer(), primary_key=True)
    assembly_id = db.Column(db.Integer(), db.ForeignKey("assembly.id"))
    assembly_component_id = db.Column(db.Integer(), db.ForeignKey("assembly_component.id"))
    dataset_id = db.Column(db.Integer(), db.ForeignKey("dataset.id"))
    kmer = db.Column(db.String())
    complete_primary = db.Column(db.Integer())
    complete_alternate = db.Column(db.Integer())
    complete_all = db.Column(db.Integer())
    qv_primary = db.Column(db.Float())
    qv_alternate = db.Column(db.Float())
    qv_all = db.Column(db.Float())
    software_version_id = db.Column(db.Integer(), db.ForeignKey("software_version.id"))
    assembly = db.relationship("TolqcAssembly", back_populates="merqury_metrics",
                               foreign_keys=[assembly_id])
    dataset = db.relationship("TolqcDataset", back_populates="merqury_metrics",
                              foreign_keys=[dataset_id])
    assembly_component = db.relationship("TolqcAssemblyComponent",
                                         back_populates="merqury_metrics",
                                         foreign_keys=[assembly_component_id])
    software_version = db.relationship("TolqcSoftwareVersion", back_populates="merqury_metrics",
                                       foreign_keys=[software_version_id])
