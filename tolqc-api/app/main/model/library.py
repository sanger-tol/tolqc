# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from tol.api_base.model import LogBase, db, setup_model


@setup_model
class Library(LogBase):
    __tablename__ = 'library'

    class Meta:
        type_ = 'libraries'

    id = db.Column(db.Integer(), primary_key=True)  # noqa A003
    name = db.Column(db.String())
    hierarchy_name = db.Column(db.String())
    library_type_id = db.Column(db.Integer(), db.ForeignKey('library_type.id'))
    lims_id = db.Column(db.Integer())
    data = db.relationship('Data', back_populates='library')
    library_type = db.relationship(
        'LibraryType', back_populates='library', foreign_keys=[library_type_id]
    )
