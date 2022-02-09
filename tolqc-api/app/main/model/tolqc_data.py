# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .log_base import LogBase, db
from .base import setup_model


@setup_model
class TolqcData(LogBase):
    __tablename__ = "data"

    class Meta:
        type_ = 'data'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    hierarchy_name = db.Column(db.String())
    sample_id = db.Column(db.Integer(), db.ForeignKey("sample.id"))
    library_id = db.Column(db.Integer(), db.ForeignKey("library.id"))
    accession_id = db.Column(db.Integer(), db.ForeignKey("accession.id"))
    run_id = db.Column(db.Integer(), db.ForeignKey("run.id"))
    processed = db.Column(db.Integer())
    tag1_id = db.Column(db.String())
    tag2_id = db.Column(db.String())
    lims_qc = db.Column(db.Integer())
    auto_qc = db.Column(db.Integer())
    qc = db.Column(db.Integer())
    withdrawn = db.Column(db.Boolean())
    manually_withdrawn = db.Column(db.Boolean())
    date = db.Column(db.DateTime())
    sample = db.relationship("TolqcSample", back_populates="data",
                             foreign_keys=[sample_id])
    library = db.relationship("TolqcLibrary", back_populates="data",
                              foreign_keys=[library_id])
    run = db.relationship("TolqcRun", back_populates="data",
                          foreign_keys=[run_id])
    accession = db.relationship("TolqcAccession", back_populates="data",
                                foreign_keys=[accession_id])
    set = db.relationship("TolqcSet", back_populates="data")
    file = db.relationship("TolqcFile", back_populates="data")
