# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .creation_log_base import CreationLogBase, db


class TolqcSeq(CreationLogBase):
    __tablename__ = "seq"
    id = db.Column(db.Integer(), primary_key=True)
    seq_id = db.Column(db.Integer(), nullable=False)
    name = db.Column(db.String(), nullable=False)
    hierarchy_name = db.Column(db.String(), nullable=False)
    sample_instance_id = db.Column(db.Integer(), db.ForeignKey("samples.id"),
                                   nullable=False)
    library_instance_id = db.Column(db.Integer(), db.ForeignKey("libraries.id"),
                                    nullable=False)
    accession_id = db.Column(db.Integer())
    run_instance_id = db.Column(db.Integer(), db.ForeignKey("runs.id"),
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
    samples = db.relationship("TolqcSample", back_populates="seq",
                             foreign_keys=[sample_instance_id])
    libraries = db.relationship("TolqcLibrary", back_populates="seq",
                              foreign_keys=[library_instance_id])
    runs = db.relationship("TolqcRun", back_populates="seq", foreign_keys=[run_instance_id])
