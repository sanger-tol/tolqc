# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from tol.api_base.model import LogBase, db, setup_model


@setup_model
class Accession(LogBase):
    __tablename__ = 'accession'

    class Meta:
        type_ = 'accessions'

    id = db.Column(db.Integer(), primary_key=True)  # noqa A003
    name = db.Column(db.String())
    accession_type_id = db.Column(db.Integer(), db.ForeignKey('accession_type_dict.id'))
    secondary = db.Column(db.String())
    submission = db.Column(db.String())
    date_submitted = db.Column(db.DateTime())
    title = db.Column(db.String())
    description = db.Column(db.String())

    accession_type_dict = db.relationship(
        'AccessionTypeDict',
        back_populates='accession',
        foreign_keys=[accession_type_id],
    )
    project = db.relationship('Project', back_populates='accession')
    specimen = db.relationship('Specimen', back_populates='accession')
    sample = db.relationship('Sample', back_populates='accession')
    data = db.relationship('Data', back_populates='accession')
