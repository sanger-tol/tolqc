# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .log_base import LogBase, db
from .base import setup_model


@setup_model
class TolqcData(LogBase):
    __tablename__ = "data"
    id = db.Column(db.Integer(), primary_key=True)
    reads = db.Column(db.String())
    bases = db.Column(db.String())
    avg_read_len = db.Column(db.Float())
    read_len_n50 = db.Column(db.Float())
    seq_data = db.relationship("TolqcSeqData", back_populates="data")
    merqury = db.relationship("TolqcMerqury", back_populates="data")
    asm = db.relationship("TolqcAsm", back_populates="data")
