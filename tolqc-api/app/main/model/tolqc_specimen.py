# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .creation_log_base import CreationLogBase, db


class TolqcSpecimen(CreationLogBase):
    __tablename__ = "specimen"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    hierarchy_name = db.Column(db.String(), nullable=False)
    species_id = db.Column(db.Integer(), db.ForeignKey("species.id"),
                                    nullable=False)
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
