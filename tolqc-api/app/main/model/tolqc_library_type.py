# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .creation_log_base import CreationLogBase, db


class TolqcLibraryType(CreationLogBase):
    __tablename__ = "library_types"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    hierarchy_name = db.Column(db.String(), nullable=False)
    kit = db.Column(db.String())
    enzyme = db.Column(db.String())
    libraries = db.relationship("TolqcLibrary", back_populates="library_types")
