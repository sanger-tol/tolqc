# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .creation_log_base import CreationLogBase, db


class TolqcSpecimen(CreationLogBase):
    __tablename__ = "specimens"
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
    allocations = db.relationship("TolqcAllocation", back_populates="specimens")
    species = db.relationship("TolqcSpecies", back_populates="specimens",
                              foreign_keys=[species_instance_id])
    samples = db.relationship("TolqcSample", back_populates="specimens")
    statuses = db.relationship("TolqcStatus", back_populates="specimens", uselist=False)
    cobionts = db.relationship("TolqcCobiont", back_populates="specimens")
    sex = db.relationship("TolqcSex", back_populates="specimens",
                          foreign_keys=[sex_id])
