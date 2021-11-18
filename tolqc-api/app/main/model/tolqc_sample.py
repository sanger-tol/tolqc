# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db


class TolqcSample(Base):
    __tablename__ = "sample"
    row_id = db.Column(db.Integer())
    sample_id = db.Column(db.String(), primary_key=True)
    name = db.Column(db.String())
    hierarchy_name = db.Column(db.String())
    lims_id = db.Column(db.String())
    specimen_id = db.Column(db.String())
    accession_id = db.Column(db.String())
    changed = db.Column(db.String())
    current = db.Column(db.String())
