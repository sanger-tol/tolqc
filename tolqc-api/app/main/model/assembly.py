# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from tol.api_base.model import LogBase, db, setup_model


@setup_model
class Assembly(LogBase):
    __tablename__ = 'assembly'

    class Meta:
        type_ = 'assemblies'

    id = db.Column(db.Integer(), primary_key=True)  # noqa A003
    dataset_id = db.Column(db.Integer(), db.ForeignKey('dataset.id'))
    name = db.Column(db.String())
    description = db.Column(db.String())
    dataset = db.relationship('Dataset', back_populates='assembly',
                              foreign_keys=[dataset_id])
    assembly_metrics = db.relationship('AssemblyMetrics', back_populates='assembly')
    busco_metrics = db.relationship('BuscoMetrics', back_populates='assembly')
    merqury_metrics = db.relationship('MerquryMetrics', back_populates='assembly')
