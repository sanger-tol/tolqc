# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db


class TolqcSample(Base):
    __tablename__ = "sample"
    row_id = db.Column(db.Integer(), primary_key=True)
    sample_id = db.Column(db.Integer())
    name = db.Column(db.String())
    hierarchy_name = db.Column(db.String())
    lims_id = db.Column(db.Integer())
    specimen_id = db.Column(db.Integer(), db.ForeignKey("specimen.specimen_id"))
    accession_id = db.Column(db.Integer())
    changed = db.Column(db.DateTime())
    current = db.Column(db.Boolean())
    specimen = db.relationship("TolqcSpecimen", back_populates="sample",
                               foreign_keys=[specimen_id])
    seq = db.relationship("TolqcSeq", back_populates="sample")
