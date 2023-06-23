# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from tol.api_base.model import LogBase, db, setup_model


@setup_model
class GenomescopeMetrics(LogBase):
    __tablename__ = 'genomescope_metrics'

    class Meta:
        type_ = 'genomescope_metrics'

    id = db.Column(db.Integer(), primary_key=True)  # noqa: A003
    dataset_id = db.Column(db.String(), db.ForeignKey('dataset.dataset_id'))
    software_version_id = db.Column(
        db.Integer(), db.ForeignKey('software_version.software_version_id')
    )
    review_id = db.Column(db.String(), db.ForeignKey('review_dict.review_id'))
    kmer = db.Column(db.Integer())
    ploidy = db.Column(db.Integer())
    homozygous = db.Column(db.Float())
    heterozygous = db.Column(db.Float())
    haploid_length = db.Column(db.Integer())
    unique_length = db.Column(db.Integer())
    repeat_length = db.Column(db.Integer())
    kcov = db.Column(db.Float())
    kcov_init = db.Column(db.Integer())
    model_fit = db.Column(db.Float())
    read_error_rate = db.Column(db.Float())
    results = db.Column(db.JSON())

    dataset = db.relationship('Dataset', back_populates='genomescope_metrics')
    software_version = db.relationship(
        'SoftwareVersion', back_populates='genomescope_metrics'
    )
    review = db.relationship('ReviewDict', back_populates='genomescope_metrics')
