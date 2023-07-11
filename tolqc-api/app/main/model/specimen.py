# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from sqlalchemy.ext.associationproxy import association_proxy

from tol.api_base.model import LogBase, db, setup_model


@setup_model
class Specimen(LogBase):
    __tablename__ = 'specimen'

    class Meta:
        type_ = 'specimens'
        id_column = 'specimen_id'

    specimen_id = db.Column(db.String(), primary_key=True)
    hierarchy_name = db.Column(db.String())
    specimen_status_id = db.Column(
        db.Integer(), db.ForeignKey('specimen_status.specimen_status_id')
    )
    species_id = db.Column(db.String(), db.ForeignKey('species.species_id'))
    lims_id = db.Column(db.Integer())
    supplied_name = db.Column(db.String())
    accession_id = db.Column(
        db.String(), db.ForeignKey('accession.accession_id')
    )
    sex_id = db.Column(db.String(), db.ForeignKey('sex.sex_id'))
    ploidy = db.Column(db.String())
    karyotype = db.Column(db.String())

    species = db.relationship('Species', back_populates='specimens')
    samples = db.relationship('Sample', back_populates='specimen')
    sex = db.relationship('Sex', back_populates='specimens')
    accession = db.relationship('Accession', back_populates='specimens')

    status = db.relationship(
        'SpecimenStatus', foreign_keys=[specimen_status_id]
    )
    status_history = db.relationship(
        'SpecimenStatus',
        primaryjoin='Specimen.specimen_id == SpecimenStatus.specimen_id',
        back_populates='specimen',
    )

    parent_assn = db.relationship(
        'Offspring',
        primaryjoin='Specimen.specimen_id == Offspring.specimen_id',
        back_populates='parent',
    )
    offspring = association_proxy('parent_assn', 'offspring')

    offspring_assn = db.relationship(
        'Offspring',
        primaryjoin='Specimen.specimen_id == Offspring.offspring_specimen_id',
        back_populates='offspring',
    )
    parents = association_proxy('offspring_assn', 'parent')
