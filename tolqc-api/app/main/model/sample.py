# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from tol.api_base.model import LogBase, db
from tol.api_base.model import setup_model


@setup_model
class TolqcSample(LogBase):
    __tablename__ = "sample"

    class Meta:
        type_ = 'samples'

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
    data = db.relationship("TolqcData", back_populates="sample")
