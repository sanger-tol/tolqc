# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .creation_log_base import CreationLogBase, db
from .base import setup_model


@setup_model
class TolqcSeqData(CreationLogBase):
    __tablename__ = "seq_data"
    id = db.Column(db.Integer(), primary_key=True)
    seq_instance_id = db.Column(db.Integer(), db.ForeignKey("seq.id"),
                                nullable=False)
    data_instance_id = db.Column(db.Integer(), db.ForeignKey("data.id"),
                                 nullable=False)
    seq = db.relationship("TolqcSeq", back_populates="seq_data",
                          foreign_keys=[seq_instance_id])
    data = db.relationship("TolqcData", back_populates="seq_data",
                           foreign_keys=[data_instance_id])
