# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db


class TolqcLibrary(Base):
    __tablename__ = "library"
    row_id = db.Column(db.Integer())
    library_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    hierarchy_name = db.Column(db.String())
    library_type_id = db.Column(db.Integer(), db.ForeignKey("library_type.library_type_id"))
    lims_id = db.Column(db.Integer())
    changed = db.Column(db.DateTime())
    current = db.Column(db.DateTime())
    seq = db.relationship("TolqcSeq", back_populates="library")
    library_type = db.relationship("TolqcLibraryType", back_populates="library")
