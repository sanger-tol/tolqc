# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .creation_log_base import CreationLogBase, db
from .base import setup_model


@setup_model
class TolqcSpecies(CreationLogBase):
    __tablename__ = "species"
    id = db.Column(db.Integer(), primary_key=True)
    species_id = db.Column(db.Integer(), nullable=False)
    name = db.Column(db.String(), nullable=False)
    hierarchy_name = db.Column(db.String(), nullable=False)
    strain = db.Column(db.String())
    common_name = db.Column(db.String())
    taxon_id = db.Column(db.Integer())
    taxon_family = db.Column(db.String())
    taxon_order = db.Column(db.String())
    taxon_phylum = db.Column(db.String())
    taxon_group = db.Column(db.String())
    genome_size = db.Column(db.Integer())
    chromosome_number = db.Column(db.Integer())
    changed = db.Column(db.DateTime())
    current = db.Column(db.Boolean())
    specimens = db.relationship("TolqcSpecimen", back_populates="species")
