# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db


class TolqcSpecimen(Base):
    __tablename__ = "specimen"
    row_id = db.Column(db.Integer())
    specimen_id = db.Column(db.String(), primary_key=True)
    name = db.Column(db.String())
    hierarchy_name = db.Column(db.String())
    species_id = db.Column(db.Integer(), db.ForeignKey("species.species_id"))
    lims_id = db.Column(db.String())
    sex_id = db.Column(db.String())
    ploidy = db.Column(db.String())
    karyotype = db.Column(db.String())
    father_id = db.Column(db.Integer())
    mother_id = db.Column(db.Integer())
    changed = db.Column(db.DateTime())
    current = db.Column(db.DateTime())
    allocation = db.relationship("TolqcAllocation", back_populates="specimen")
    species = db.relationship("TolqcSpecies", back_populates="specimen")
    sample = db.relationship("TolqcSample", back_populates="specimen")
