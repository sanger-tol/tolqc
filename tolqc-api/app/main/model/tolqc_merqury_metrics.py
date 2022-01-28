# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .creation_log_base import CreationLogBase, db


class TolqcMerquryMetrics(CreationLogBase):
    __tablename__ = "merqury_metrics"
    id = db.Column(db.Integer(), primary_key=True)
    assembly_id = db.Column(db.Integer(), db.ForeignKey("assembly.id"))
    assembly_component_id = db.Column(db.Integer(), db.ForeignKey("assembly_component.id"))
    data_id = db.Column(db.Integer(), db.ForeignKey("data.id"))
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
    data = db.relationship("TolqcData", back_populates="merqury_metrics", foreign_keys=[data_id])
    assembly_component = db.relationship("TolqcAssemblyComponent", 
                                         back_populates="merqury_metrics",
                                         foreign_keys=[assembly_component_id])
    software_version = db.relationship("TolqcSoftwareVersion", back_populates="merqury_metrics",
                                       foreign_keys=[software_version_id])
