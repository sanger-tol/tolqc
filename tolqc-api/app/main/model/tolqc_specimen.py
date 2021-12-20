# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .sub_base import SubBase, db


class TolqcSpecimen(SubBase):
    __tablename__ = "specimen"
    id = db.Column(db.Integer(), primary_key=True)
    specimen_id = db.Column(db.Integer(), nullable=False)
    name = db.Column(db.String(), nullable=False)
    hierarchy_name = db.Column(db.String(), nullable=False)
    species_instance_id = db.Column(db.Integer(), db.ForeignKey("species.id"),
                                    nullable=False)
    lims_id = db.Column(db.Integer())
    supplier_name = db.Column(db.String())
    accession_id = db.Column(db.Integer())
    sex_id = db.Column(db.Integer(), db.ForeignKey("sex.id"))
    ploidy = db.Column(db.String())
    karyotype = db.Column(db.String())
    father_id = db.Column(db.Integer())
    mother_id = db.Column(db.Integer())
    changed = db.Column(db.DateTime())
    current = db.Column(db.Boolean())
    allocation = db.relationship("TolqcAllocation", back_populates="specimen")
    species = db.relationship("TolqcSpecies", back_populates="specimen",
                              foreign_keys=[species_instance_id])
    sample = db.relationship("TolqcSample", back_populates="specimen")
    status = db.relationship("TolqcStatus", back_populates="specimen", uselist=False)
    cobiont = db.relationship("TolqcCobiont", back_populates="specimen")
    sex = db.relationship("TolqcSex", back_populates="specimen",
                          foreign_keys=[sex_id])
