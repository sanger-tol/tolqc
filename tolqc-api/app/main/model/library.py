# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from tol.api_base.model import Base, db, setup_model


@setup_model
class Library(Base):
    __tablename__ = 'library'

    class Meta:
        type_ = 'libraries'
        id_column = 'library_id'

    library_id = db.Column(db.String(), primary_key=True)
    library_type_id = db.Column(
        db.String(), db.ForeignKey('library_type.library_type_id')
    )
    lims_id = db.Column(db.Integer())

    data = db.relationship('Data', back_populates='library')
    library_type = db.relationship('LibraryType', back_populates='library')
