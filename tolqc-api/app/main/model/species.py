# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from tol.api_base.model import LogBase, db, setup_model


@setup_model
class Species(LogBase):
    __tablename__ = 'species'

    class Meta:
        type_ = 'species'
        id_column = 'species_id'

    species_id = db.Column(db.String(), primary_key=True)
    hierarchy_name = db.Column(db.String(), nullable=False, unique=True)
    strain = db.Column(db.String())
    common_name = db.Column(db.String())
    taxon_id = db.Column(db.Integer(), index=True)
    taxon_family = db.Column(db.String())
    taxon_order = db.Column(db.String())
    taxon_phylum = db.Column(db.String())
    taxon_group = db.Column(db.String())
    genome_size = db.Column(db.BigInteger())
    chromosome_number = db.Column(db.Integer())

    specimens = db.relationship('Specimen', back_populates='species')
