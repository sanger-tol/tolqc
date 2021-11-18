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
    library_type_id = db.Column(db.Integer())
    lims_id = db.Column(db.Integer())
    changed = db.Column(db.DateTime())
    current = db.Column(db.DateTime())
