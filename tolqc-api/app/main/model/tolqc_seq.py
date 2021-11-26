# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db


class TolqcSeq(Base):
    __tablename__ = "seq"
    id = db.Column(db.Integer(), primary_key=True)
    seq_id = db.Column(db.Integer(), nullable=False)
    name = db.Column(db.String(), nullable=False)
    hierarchy_name = db.Column(db.String(), nullable=False)
    sample_row_id = db.Column(db.Integer(), db.ForeignKey("sample.id"),
                              nullable=False)
    library_row_id = db.Column(db.Integer(), db.ForeignKey("library.id"),
                               nullable=False)
    accession_id = db.Column(db.Integer())
    run_row_id = db.Column(db.Integer(), db.ForeignKey("run.id"),
                           nullable=False)
    processed = db.Column(db.Integer())
    tag1_id = db.Column(db.String())
    tag2_id = db.Column(db.String())
    lims_qc = db.Column(db.Integer())
    auto_qc = db.Column(db.Integer())
    qc = db.Column(db.Integer())
    withdrawn = db.Column(db.Boolean())
    manually_withdrawn = db.Column(db.Boolean())
    date = db.Column(db.DateTime())
    changed = db.Column(db.DateTime())
    current = db.Column(db.Boolean())
    sample = db.relationship("TolqcSample", back_populates="seq", foreign_keys=[sample_row_id])
    library = db.relationship("TolqcLibrary", back_populates="seq", foreign_keys=[library_row_id])
    run = db.relationship("TolqcRun", back_populates="seq", foreign_keys=[run_row_id])
