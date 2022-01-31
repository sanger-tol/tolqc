# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .log_base import LogBase, db


class TolqcSet(LogBase):
    __tablename__ = "set"
    id = db.Column(db.Integer(), primary_key=True)
    data_id = db.Column(db.Integer(), db.ForeignKey("data.id"))
    dataset_id = db.Column(db.Integer(), db.ForeignKey("dataset.id"))
    data = db.relationship("TolqcData", back_populates="set",
                           foreign_keys=[data_id])
    dataset = db.relationship("TolqcDataset", back_populates="set",
                              foreign_keys=[dataset_id])
