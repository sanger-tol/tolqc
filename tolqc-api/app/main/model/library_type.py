# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from tol.api_base.model import Base, db, setup_model


@setup_model
class LibraryType(Base):
    __tablename__ = 'library_type'

    class Meta:
        type_ = 'library_types'
        id_column = 'library_type_id'

    library_type_id = db.Column(db.String(), primary_key=True)
    hierarchy_name = db.Column(db.String())
    category = db.Column(db.String())
    kit = db.Column(db.String())
    enzymes = db.Column(db.String())
    cut_sites = db.Column(db.String())

    library = db.relationship('Library', back_populates='library_type')
