# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from tol.api_base.model import Base, db, setup_model


@setup_model
class AccessionTypeDict(Base):
    __tablename__ = 'accession_type_dict'

    class Meta:
        type_ = 'accession_types'
        id_column = 'accession_type_id'

    accession_type_id = db.Column(db.String(), primary_key=True)
    regexp = db.Column(db.String())
    url = db.Column(db.String())

    accessions = db.relationship('Accession', back_populates='accession_type')
