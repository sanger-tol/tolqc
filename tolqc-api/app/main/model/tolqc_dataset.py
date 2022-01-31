# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .log_base import LogBase, db


class TolqcDataset(LogBase):
    __tablename__ = "dataset"
    id = db.Column(db.Integer(), primary_key=True)
    reads = db.Column(db.Integer())
    bases = db.Column(db.Integer())
    avg_read_len = db.Column(db.Float())
    read_len_n50 = db.Column(db.Float())
    set = db.relationship("TolqcSet", back_populates="dataset")
    merqury_metrics = db.relationship("TolqcMerquryMetrics", back_populates="dataset")
    assembly = db.relationship("TolqcAssembly", back_populates="dataset")
    genomescope_metrics = db.relationship("TolqcGenomescopeMetrics",
                                          back_populates="dataset")
