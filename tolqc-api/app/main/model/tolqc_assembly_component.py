# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .log_base import LogBase, db
from .enum_base import EnumBase
from .base import setup_model


@setup_model
class TolqcAssemblyComponent(LogBase, EnumBase):
    __tablename__ = "assembly_component"

    busco_metrics = db.relationship("TolqcBuscoMetrics",
                                    back_populates="assembly_component")
    merqury_metrics = db.relationship("TolqcMerquryMetrics",
                                      back_populates="assembly_component")
    assembly_metrics = db.relationship("TolqcAssemblyMetrics",
                                       back_populates="assembly_component")
