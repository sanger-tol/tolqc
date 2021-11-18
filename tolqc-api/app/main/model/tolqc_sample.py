# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db


class TolqcSample(Base):
    __tablename__ = "sample"
    row_id = db.Column(db.Integer())
    sample_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    hierarchy_name = db.Column(db.String())
    lims_id = db.Column(db.Integer())
    specimen_id = db.Column(db.Integer())
    accession_id = db.Column(db.String())
    changed = db.Column(db.DateTime())
    current = db.Column(db.DateTime())
