# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .log_base import LogBase, db
from .base import setup_model


@setup_model
class TolqcMerqury(LogBase):
    __tablename__ = "merqury"
    id = db.Column(db.Integer(), primary_key=True)
    asm_stats_instance_id = db.Column(db.Integer(), db.ForeignKey("asm_stats.id"),
                                      nullable=False)
    data_id = db.Column(db.Integer(), db.ForeignKey("data.id"),
                        nullable=False)
    kmer = db.Column(db.String())
    complete_primary = db.Column(db.Boolean())
    complete_alternate = db.Column(db.Boolean())
    complete_all = db.Column(db.Boolean())
    qv_primary = db.Column(db.String())
    qv_alternate = db.Column(db.String())
    qv_all = db.Column(db.String())
    software_version_instance_id = db.Column(db.Integer(),
                                             db.ForeignKey("software_versions.id"),
                                             nullable=False)
    asm_stats = db.relationship("TolqcAsmStats", back_populates="merqury",
                                foreign_keys=[asm_stats_instance_id])
    data = db.relationship("TolqcData", back_populates="merqury", foreign_keys=[data_id])
    software_versions = db.relationship("TolqcSoftwareVersion", back_populates="merqury",
                                        foreign_keys=[software_version_instance_id])
