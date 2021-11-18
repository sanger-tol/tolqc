# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db


class TolqcRun(Base):
    __tablename__ = "run"
    row_id = db.Column(db.Integer())
    run_id = db.Column(db.String(), primary_key=True)
    name = db.Column(db.String())
    hierarchy_name = db.Column(db.String())
    platform_id = db.Column(db.String())
    centre_id = db.Column(db.String())
    lims_id = db.Column(db.String())
    element = db.Column(db.String())
    changed = db.Column(db.String())
    current = db.Column(db.String())
