# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from tol.api_base.model import LogBase, db, setup_model


@setup_model
class Species(LogBase):
    __tablename__ = 'species'

    class Meta:
        type_ = 'species'

    id = db.Column(db.Integer(), primary_key=True)  # noqa A003
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
    specimen = db.relationship('Specimen', back_populates='species')
