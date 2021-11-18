# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db


class TolqcSpecies(Base):
    __tablename__ = "species"
    row_id = db.Column(db.Integer())
    species_id = db.Column(db.String(), primary_key=True)
    name = db.Column(db.String())
    hierarchy_name = db.Column(db.String())
    strain = db.Column(db.String())
    common_name = db.Column(db.String())
    taxon_id = db.Column(db.String())
    taxon_family = db.Column(db.Float())
    taxon_order = db.Column(db.Integer())
    taxon_phylum = db.Column(db.Integer())
    taxon_group = db.Column(db.DateTime())
    genome_size = db.Column(db.Integer())
    chromosome_number = db.Column(db.String())
    changed = db.Column(db.DateTime())
    current = db.Column(db.DateTime())
