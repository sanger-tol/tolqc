# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .log_base import LogBase, db


class TolqcSeqData(LogBase):
    __tablename__ = "seq_data"
    id = db.Column(db.Integer(), primary_key=True)
    seq_instance_id = db.Column(db.Integer(), db.ForeignKey("seq.id"))
    data_instance_id = db.Column(db.Integer(), db.ForeignKey("data.id"))
    seq = db.relationship("TolqcSeq", back_populates="seq_data",
                          foreign_keys=[seq_instance_id])
    data = db.relationship("TolqcData", back_populates="seq_data",
                           foreign_keys=[data_instance_id])
