# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db


class TolqcLibrary(Base):
    __tablename__ = "library"
    row_id = db.Column(db.Integer(), primary_key=True)
    library_id = db.Column(db.String())
    name = db.Column(db.String())
    hierarchy_name = db.Column(db.String())
    library_type_id = db.Column(db.String())
    lims_id = db.Column(db.String())
    changed = db.Column(db.String())
    current = db.Column(db.String())
