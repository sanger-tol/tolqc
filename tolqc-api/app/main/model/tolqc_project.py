# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db


class TolqcProject(Base):
    __tablename__ = "project"
    project_id = db.Column(db.String(), primary_key=True)
    name = db.Column(db.String())
    hierarchy_name = db.Column(db.String())
    description = db.Column(db.String())
    lims_id = db.Column(db.String())
    accession_id = db.Column(db.String())
