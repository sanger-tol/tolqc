# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db


class TolqcSample(Base):
    __tablename__ = "sample"
    row_id = db.Column(db.Integer(), primary_key=True)
    sample_id = db.Column(db.Integer(), nullable=False)
    name = db.Column(db.String(), nullable=False)
    hierarchy_name = db.Column(db.String(), nullable=False)
    lims_id = db.Column(db.Integer())
    specimen_row_id = db.Column(db.Integer(), db.ForeignKey("specimen.row_id"),
                                nullable=False)
    accession_id = db.Column(db.Integer())
    changed = db.Column(db.DateTime())
    current = db.Column(db.Boolean())
    specimen = db.relationship("TolqcSpecimen", back_populates="sample",
                               foreign_keys=[specimen_row_id])
    seq = db.relationship("TolqcSeq", back_populates="sample")
