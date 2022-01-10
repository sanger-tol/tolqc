# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .creation_log_base import CreationLogBase, db


class TolqcLibrary(CreationLogBase):
    __tablename__ = "library"
    id = db.Column(db.Integer(), primary_key=True)
    library_id = db.Column(db.Integer(), nullable=False)
    name = db.Column(db.String(), nullable=False)
    hierarchy_name = db.Column(db.String(), nullable=False)
    library_type_id = db.Column(db.Integer(), db.ForeignKey("library_type.id"),
                                nullable=False)
    lims_id = db.Column(db.Integer())
    changed = db.Column(db.DateTime())
    current = db.Column(db.Boolean())
    seq = db.relationship("TolqcSeq", back_populates="library")
    library_type = db.relationship("TolqcLibraryType", back_populates="library",
                                   foreign_keys=[library_type_id])
