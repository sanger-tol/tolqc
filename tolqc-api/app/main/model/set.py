# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from tol.api_base.model import LogBase, db, setup_model


@setup_model
class Set(LogBase):
    __tablename__ = 'set'

    class Meta:
        type_ = 'sets'

    id = db.Column(db.Integer(), primary_key=True)  # noqa A003
    data_id = db.Column(db.Integer(), db.ForeignKey('data.id'))
    dataset_id = db.Column(db.Integer(), db.ForeignKey('dataset.id'))
    data = db.relationship('Data', back_populates='set', foreign_keys=[data_id])
    dataset = db.relationship(
        'Dataset', back_populates='set', foreign_keys=[dataset_id]
    )
