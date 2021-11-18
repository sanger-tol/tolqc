# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db


class TolqcLibraryType(Base):
    __tablename__ = "library_type"
    library_type_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    hierarchy_name = db.Column(db.String())
    kit = db.Column(db.String())
    enzyme = db.Column(db.String())
