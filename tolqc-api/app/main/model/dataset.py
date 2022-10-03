# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .tol.api_base.model import LogBase, db
from .tol.api_base.model import setup_model


@setup_model
class TolqcDataset(LogBase):
    __tablename__ = "dataset"

    class Meta:
        type_ = 'datasets'

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
