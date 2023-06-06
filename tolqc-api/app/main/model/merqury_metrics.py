# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from tol.api_base.model import LogBase, db, setup_model


@setup_model
class MerquryMetrics(LogBase):
    __tablename__ = 'merqury_metrics'

    class Meta:
        type_ = 'merqury_metrics'

    id = db.Column(db.Integer(), primary_key=True)  # noqa A003
    assembly_id = db.Column(db.Integer(), db.ForeignKey('assembly.id'))
    assembly_component_id = db.Column(
        db.Integer(), db.ForeignKey('assembly_component.id')
    )
    dataset_id = db.Column(db.Integer(), db.ForeignKey('dataset.id'))
    kmer = db.Column(db.String())
    complete_primary = db.Column(db.Integer())
    complete_alternate = db.Column(db.Integer())
    complete_all = db.Column(db.Integer())
    qv_primary = db.Column(db.Float())
    qv_alternate = db.Column(db.Float())
    qv_all = db.Column(db.Float())
    software_version_id = db.Column(db.Integer(), db.ForeignKey('software_version.id'))
    assembly = db.relationship(
        'Assembly', back_populates='merqury_metrics', foreign_keys=[assembly_id]
    )
    dataset = db.relationship(
        'Dataset', back_populates='merqury_metrics', foreign_keys=[dataset_id]
    )
    assembly_component = db.relationship(
        'AssemblyComponent',
        back_populates='merqury_metrics',
        foreign_keys=[assembly_component_id],
    )
    software_version = db.relationship(
        'SoftwareVersion',
        back_populates='merqury_metrics',
        foreign_keys=[software_version_id],
    )
