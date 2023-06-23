# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from tol.api_base.model import Base, db, setup_model


@setup_model
class Accession(Base):
    __tablename__ = 'accession'

    class Meta:
        type_ = 'accessions'
        id_column = 'accession_id'

    accession_id = db.Column(db.String(), primary_key=True)
    accession_type_id = db.Column(
        db.String(), db.ForeignKey('accession_type_dict.accession_type_id')
    )
    secondary = db.Column(db.String())
    submission = db.Column(db.String())
    date_submitted = db.Column(db.DateTime())
    title = db.Column(db.String())
    description = db.Column(db.String())

    accession_type = db.relationship('AccessionTypeDict', back_populates='accessions')
    projects = db.relationship('Project', back_populates='accession')
    specimens = db.relationship('Specimen', back_populates='accession')
    samples = db.relationship('Sample', back_populates='accession')
    data = db.relationship('Data', back_populates='accession')
