# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .creation_log_base import CreationLogBase, db


class TolqcSample(CreationLogBase):
    __tablename__ = "sample"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    hierarchy_name = db.Column(db.String())
    lims_id = db.Column(db.Integer())
    specimen_id = db.Column(db.Integer(), db.ForeignKey("specimen.id"))
    accession_id = db.Column(db.Integer(), db.ForeignKey("accession.id"))
    specimen = db.relationship("TolqcSpecimen", back_populates="sample",
                               foreign_keys=[specimen_id])
    accession = db.relationship("TolqcAccession", back_populates="sample",
                               foreign_keys=[accession_id])
    seq = db.relationship("TolqcSeq", back_populates="sample")
