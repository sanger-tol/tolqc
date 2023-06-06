# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from tol.api_base.model import LogBase, db, setup_model


@setup_model
class Specimen(LogBase):
    __tablename__ = 'specimen'

    class Meta:
        type_ = 'specimens'

    id = db.Column(db.Integer(), primary_key=True)  # noqa A003
    name = db.Column(db.String())
    hierarchy_name = db.Column(db.String())
    species_id = db.Column(db.Integer(), db.ForeignKey('species.id'))
    lims_id = db.Column(db.Integer())
    supplied_name = db.Column(db.String())
    accession_id = db.Column(db.Integer(), db.ForeignKey('accession.id'))
    sex_id = db.Column(db.Integer(), db.ForeignKey('sex.id'))
    ploidy = db.Column(db.String())
    karyotype = db.Column(db.String())
    father_id = db.Column(db.Integer())
    mother_id = db.Column(db.Integer())
    allocation = db.relationship('Allocation', back_populates='specimen')
    species = db.relationship(
        'Species', back_populates='specimen', foreign_keys=[species_id]
    )
    sample = db.relationship('Sample', back_populates='specimen')
    status = db.relationship('Status', back_populates='specimen', uselist=False)
    sex = db.relationship('Sex', back_populates='specimen', foreign_keys=[sex_id])
    accession = db.relationship(
        'Accession', back_populates='specimen', foreign_keys=[accession_id]
    )
