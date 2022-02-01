# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .log_base import LogBase, db
from .base import setup_model


@setup_model
class TolqcSpecimen(LogBase):
    __tablename__ = "specimen"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    hierarchy_name = db.Column(db.String())
    species_id = db.Column(db.Integer(), db.ForeignKey("species.id"))
    lims_id = db.Column(db.Integer())
    supplied_name = db.Column(db.String())
    accession_id = db.Column(db.Integer(), db.ForeignKey("accession.id"))
    sex_id = db.Column(db.Integer(), db.ForeignKey("sex.id"))
    ploidy = db.Column(db.String())
    karyotype = db.Column(db.String())
    father_id = db.Column(db.Integer())
    mother_id = db.Column(db.Integer())
    allocation = db.relationship("TolqcAllocation", back_populates="specimen")
    species = db.relationship("TolqcSpecies", back_populates="specimen",
                              foreign_keys=[species_id])
    sample = db.relationship("TolqcSample", back_populates="specimen")
    status = db.relationship("TolqcStatus", back_populates="specimen", uselist=False)
    sex = db.relationship("TolqcSex", back_populates="specimen",
                          foreign_keys=[sex_id])
    accession = db.relationship("TolqcAccession", back_populates="specimen",
                                foreign_keys=[accession_id])
