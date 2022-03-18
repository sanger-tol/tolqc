# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db, LogMixin, setup_model


@setup_model
class TolqcSet(Base, LogMixin):
    __tablename__ = "set"

    class Meta:
        type_ = 'sets'

    id = db.Column(db.Integer(), primary_key=True)
    data_id = db.Column(db.Integer(), db.ForeignKey("data.id"))
    dataset_id = db.Column(db.Integer(), db.ForeignKey("dataset.id"))
    data = db.relationship("TolqcData", back_populates="set",
                           foreign_keys=[data_id])
    dataset = db.relationship("TolqcDataset", back_populates="set",
                              foreign_keys=[dataset_id])
