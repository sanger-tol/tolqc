# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from tol.api_base.model import LogBase, db, setup_model


@setup_model
class Dataset(LogBase):
    __tablename__ = 'dataset'

    class Meta:
        type_ = 'datasets'

    id = db.Column(db.Integer(), primary_key=True)  # noqa A003
    reads = db.Column(db.Integer())
    bases = db.Column(db.Integer())
    avg_read_len = db.Column(db.Float())
    read_len_n50 = db.Column(db.Float())
    set = db.relationship('Set', back_populates='dataset')  # noqa A003
    merqury_metrics = db.relationship('MerquryMetrics', back_populates='dataset')
    assembly = db.relationship('Assembly', back_populates='dataset')
    genomescope_metrics = db.relationship('GenomescopeMetrics',
                                          back_populates='dataset')
