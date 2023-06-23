# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from tol.api_base.model import Base, db, setup_model


@setup_model
class MerquryMetrics(Base):
    __tablename__ = 'merqury_metrics'

    class Meta:
        type_ = 'merqury_metrics'

    id = db.Column(db.Integer(), primary_key=True)  # noqa: A003
    assembly_id = db.Column(db.Integer(), db.ForeignKey('assembly.assembly_id'))
    dataset_id = db.Column(db.String(), db.ForeignKey('dataset.dataset_id'))
    kmer = db.Column(db.String())
    complete_primary = db.Column(db.Integer())
    complete_alternate = db.Column(db.Integer())
    complete_all = db.Column(db.Integer())
    qv_primary = db.Column(db.Float())
    qv_alternate = db.Column(db.Float())
    qv_all = db.Column(db.Float())
    software_version_id = db.Column(
        db.Integer(), db.ForeignKey('software_version.software_version_id')
    )

    assembly = db.relationship('Assembly', back_populates='merqury_metrics')
    dataset = db.relationship('Dataset', back_populates='merqury_metrics')
    software_version = db.relationship(
        'SoftwareVersion',
        back_populates='merqury_metrics',
    )
