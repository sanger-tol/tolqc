# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from tol.api_base.model import Base, db, setup_model


@setup_model
class PloidyplotMetrics(Base):
    __tablename__ = 'ploidyplot_metrics'

    class Meta:
        type_ = 'ploidyplot_metrics'

    id = db.Column(db.Integer(), primary_key=True)  # noqa: A003
    dataset_id = db.Column(db.String(), db.ForeignKey('dataset.dataset_id'))
    kmer = db.Column(db.Integer())
    ploidy = db.Column(db.Integer())
    n = db.Column(db.Float())
    partition = db.Column(db.String())
    trim_threshold = db.Column(db.Integer())
    software_version_id = db.Column(
        db.Integer(), db.ForeignKey('software_version.software_version_id')
    )

    dataset = db.relationship('Dataset', back_populates='ploidyplot_metrics')
    software_version = db.relationship(
        'SoftwareVersion', back_populates='ploidyplot_metrics'
    )
