# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .creation_log_base import CreationLogBase, db


class TolqcBusco(CreationLogBase):
    __tablename__ = "busco"
    id = db.Column(db.Integer(), primary_key=True)
    asm_stats_instance_id = db.Column(db.Integer(), db.ForeignKey("asm_stats.id"),
                                      nullable=False)
    complete = db.Column(db.Boolean())
    single = db.Column(db.Boolean())
    duplicated = db.Column(db.Boolean())
    fragmented = db.Column(db.Boolean())
    missing = db.Column(db.Boolean())
    linage = db.Column(db.String())
    software_version_instance_id = db.Column(db.Integer(),
                                             db.ForeignKey("software_versions.id"),
                                             nullable=False)
    asm_stats = db.relationship("TolqcAsmStats", back_populates="busco",
                                foreign_keys=[asm_stats_instance_id])
    software_versions = db.relationship("TolqcSoftwareVersion", back_populates="busco",
                                        foreign_keys=[software_version_instance_id])
