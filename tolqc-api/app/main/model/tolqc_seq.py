# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db


class TolqcSeq(Base):
    __tablename__ = "seq"
    row_id = db.Column(db.Integer())
    seq_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    hierarchy_name = db.Column(db.String())
    sample_id = db.Column(db.String())
    library_id = db.Column(db.Integer())
    accession_id = db.Column(db.Integer())
    run_id = db.Column(db.Integer())
    processed = db.Column(db.String())
    tag1_id = db.Column(db.String())
    tag2_id = db.Column(db.String())
    lims_qc = db.Column(db.Integer())
    auto_qc = db.Column(db.String())
    qc = db.Column(db.String())
    withdrawn = db.Column(db.String())
    manually_withdrawn = db.Column(db.String())
    date = db.Column(db.DateTime())
    changed = db.Column(db.DateTime())
    current = db.Column(db.DateTime())
