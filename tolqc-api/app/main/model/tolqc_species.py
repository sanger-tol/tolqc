# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .log_base import LogBase, db


class TolqcSpecies(LogBase):
    __tablename__ = "species"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    hierarchy_name = db.Column(db.String())
    strain = db.Column(db.String())
    common_name = db.Column(db.String())
    taxon_id = db.Column(db.Integer())
    taxon_family = db.Column(db.String())
    taxon_order = db.Column(db.String())
    taxon_phylum = db.Column(db.String())
    taxon_group = db.Column(db.String())
    genome_size = db.Column(db.Integer())
    chromosome_number = db.Column(db.Integer())
    specimen = db.relationship("TolqcSpecimen", back_populates="species")
