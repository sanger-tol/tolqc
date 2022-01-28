# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .log_base import LogBase, db


class TolqcLibrary(LogBase):
    __tablename__ = "library"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    hierarchy_name = db.Column(db.String())
    library_type_id = db.Column(db.Integer(), db.ForeignKey("library_type.id"))
    lims_id = db.Column(db.Integer())
    seq = db.relationship("TolqcSeq", back_populates="library")
    library_type = db.relationship("TolqcLibraryType", back_populates="library",
                                   foreign_keys=[library_type_id])
