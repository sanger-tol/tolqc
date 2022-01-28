# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .log_base import LogBase, db


class TolqcAssemblyComponent(LogBase):
    __tablename__ = "assembly_component"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String())
    busco_metrics = db.relationship("TolqcBuscoMetrics",
                                    back_populates="assembly_component")
    merqury_metrics = db.relationship("TolqcMerquryMetrics",
                                      back_populates="assembly_component")
    assembly_metrics = db.relationship("TolqcAssemblyMetrics",
                                       back_populates="assembly_component")
