# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .log_base import LogBase, db
from .base import setup_model


@setup_model
class TolqcBuscoMetrics(LogBase):
    __tablename__ = "busco_metrics"

    class Meta:
        type_ = 'busco_metrics'

    id = db.Column(db.Integer(), primary_key=True)
    assembly_id = db.Column(db.Integer(), db.ForeignKey("assembly.id"))
    assembly_component_id = db.Column(db.Integer(), db.ForeignKey("assembly_component.id"))
    complete = db.Column(db.Integer())
    single = db.Column(db.Integer())
    duplicated = db.Column(db.Integer())
    fragmented = db.Column(db.Integer())
    missing = db.Column(db.Integer())
    count = db.Column(db.Integer())
    busco_lineage_id = db.Column(db.Integer(), db.ForeignKey("busco_lineage.id"))
    summary = db.Column(db.String())
    software_version_id = db.Column(db.Integer(), db.ForeignKey("software_version.id"))
    assembly = db.relationship("TolqcAssembly", back_populates="busco_metrics",
                               foreign_keys=[assembly_id])
    assembly_component = db.relationship("TolqcAssemblyComponent",
                                         back_populates="busco_metrics",
                                         foreign_keys=[assembly_component_id])
    busco_lineage = db.relationship("TolqcBuscoLineage", back_populates="busco_metrics",
                                    foreign_keys=[busco_lineage_id])
    software_version = db.relationship("TolqcSoftwareVersion", back_populates="busco_metrics",
                                       foreign_keys=[software_version_id])
