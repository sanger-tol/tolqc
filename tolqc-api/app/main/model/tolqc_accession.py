# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .creation_log_base import CreationLogBase, db


class TolqcAccession(CreationLogBase):
    __tablename__ = "accession"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    accession_type_id = db.Column(db.Integer(), db.ForeignKey("accession_type_dict.id"))
    secondary = db.Column(db.String())
    submission = db.Column(db.String())
    date_submitted = db.Column(db.DateTime())
    title = db.Column(db.String())
    description = db.Column(db.String())

    accession_type = db.relationship("TolqcAccessionTypeDict", back_populates="accession",
                                     foreign_keys=[accession_type_id])
    project = db.relationship("TolqcProject", back_populates="accession")
    specimen = db.relationship("TolqcSpecimen", back_populates="accession")
    sample = db.relationship("TolqcSample", back_populates="accession")
    seq = db.relationship("TolqcSeq", back_populates="accession")
