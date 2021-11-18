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
    species_id = db.Column(db.String())
    lims_id = db.Column(db.String())
    sex_id = db.Column(db.String())
    ploidy = db.Column(db.String())
    karyotype = db.Column(db.String())
    father_id = db.Column(db.String())
    mother_id = db.Column(db.String())
    changed = db.Column(db.String())
    current = db.Column(db.String())
