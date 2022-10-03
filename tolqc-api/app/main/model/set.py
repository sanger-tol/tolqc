# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .log_base import LogBase, db
from .base import setup_model


@setup_model
class TolqcSet(LogBase):
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
