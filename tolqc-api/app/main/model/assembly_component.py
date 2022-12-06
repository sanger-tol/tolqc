# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from tol.api_base.model import EnumBase, LogBase, db, setup_model


@setup_model
class TolqcAssemblyComponent(LogBase, EnumBase):
    __tablename__ = 'assembly_component'

    class Meta:
        type_ = 'assembly_components'

    busco_metrics = db.relationship('TolqcBuscoMetrics',
                                    back_populates='assembly_component')
    merqury_metrics = db.relationship('TolqcMerquryMetrics',
                                      back_populates='assembly_component')
    assembly_metrics = db.relationship('TolqcAssemblyMetrics',
                                       back_populates='assembly_component')
