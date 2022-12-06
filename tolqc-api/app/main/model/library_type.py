# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from tol.api_base.model import Base, db, setup_model


@setup_model
class TolqcLibraryType(Base):
    __tablename__ = 'library_type'

    class Meta:
        type_ = 'library_types'

    id = db.Column(db.Integer(), primary_key=True)  # noqa A003
    name = db.Column(db.String())
    hierarchy_name = db.Column(db.String())
    kit = db.Column(db.String())
    enzyme = db.Column(db.String())
    library = db.relationship('TolqcLibrary', back_populates='library_type')
