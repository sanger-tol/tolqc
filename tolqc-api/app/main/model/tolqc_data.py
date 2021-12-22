# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .sub_base import SubBase, db


class TolqcData(SubBase):
    __tablename__ = "data"
    id = db.Column(db.Integer(), primary_key=True)
    reads = db.Column(db.String())
    bases = db.Column(db.String())
    avg_read_len = db.Column(db.Float())
    read_len_n50 = db.Column(db.Float())
    seq_data = db.relationship("TolqcSeqData", back_populates="data")
