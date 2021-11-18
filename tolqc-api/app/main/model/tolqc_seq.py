# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db


class TolqcSeq(Base):
    __tablename__ = "seq"
    row_id = db.Column(db.Integer())
    seq_id = db.Column(db.String(), primary_key=True)
    name = db.Column(db.String())
    hierarchy_name = db.Column(db.String())
    sample_id = db.Column(db.String())
    library_id = db.Column(db.String())
    accession_id = db.Column(db.String())
    run_id = db.Column(db.String())
    processed = db.Column(db.String())
    tag1_id = db.Column(db.String())
    tag2_id = db.Column(db.String())
    lims_qc = db.Column(db.String())
    auto_qc = db.Column(db.String())
    qc = db.Column(db.String())
    withdrawn = db.Column(db.String())
    manually_withdrawn = db.Column(db.String())
    date = db.Column(db.String())
    changed = db.Column(db.String())
    current = db.Column(db.String())
