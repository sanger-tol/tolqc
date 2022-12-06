# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from tol.api_base.model import LogBase, db, setup_model


@setup_model
class TolqcAssembly(LogBase):
    __tablename__ = 'assembly'

    class Meta:
        type_ = 'assemblies'

    id = db.Column(db.Integer(), primary_key=True)  # noqa A003
    dataset_id = db.Column(db.Integer(), db.ForeignKey('dataset.id'))
    name = db.Column(db.String())
    description = db.Column(db.String())
    dataset = db.relationship('TolqcDataset', back_populates='assembly',
                              foreign_keys=[dataset_id])
    assembly_metrics = db.relationship('TolqcAssemblyMetrics', back_populates='assembly')
    busco_metrics = db.relationship('TolqcBuscoMetrics', back_populates='assembly')
    merqury_metrics = db.relationship('TolqcMerquryMetrics', back_populates='assembly')
