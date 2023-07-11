# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from sqlalchemy.ext.associationproxy import association_proxy

from tol.api_base.model import LogBase, db, setup_model


@setup_model
class Dataset(LogBase):
    __tablename__ = 'dataset'

    class Meta:
        type_ = 'datasets'
        id_column = 'dataset_id'

    dataset_id = db.Column(db.String(), primary_key=True)
    dataset_status_id = db.Column(
        db.Integer(), db.ForeignKey('dataset_status.dataset_status_id')
    )
    dataset_list_md5 = db.Column(db.String())
    reads = db.Column(db.Integer())
    bases = db.Column(db.BigInteger())
    read_length_mean = db.Column(db.Float())
    read_length_n50 = db.Column(db.Integer())

    assembly = db.relationship('Assembly', back_populates='dataset')
    genomescope_metrics = db.relationship(
        'GenomescopeMetrics', back_populates='dataset'
    )
    merqury_metrics = db.relationship(
        'MerquryMetrics', back_populates='dataset'
    )
    ploidyplot_metrics = db.relationship(
        'PloidyplotMetrics', back_populates='dataset'
    )

    status = db.relationship('DatasetStatus', foreign_keys=[dataset_status_id])
    status_history = db.relationship(
        'DatasetStatus',
        primaryjoin='Dataset.dataset_id == DatasetStatus.dataset_id',
        back_populates='dataset',
    )

    data_assn = db.relationship('DatasetElement', back_populates='dataset')
    data = association_proxy('data_assn', 'data')
