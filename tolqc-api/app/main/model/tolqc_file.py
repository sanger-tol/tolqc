# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .log_base import LogBase, db


class TolqcFile(LogBase):
    __tablename__ = "file"
    id = db.Column(db.Integer(), primary_key=True)
    data_id = db.Column(db.Integer(), db.ForeignKey("data.id"))
    name = db.Column(db.String())
    type = db.Column(db.String())
    md5 = db.Column(db.String())
    data = db.relationship("TolqcData", back_populates="file",
                           foreign_keys=[data_id])
