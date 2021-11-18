# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db


class TolqcAllocation(Base):
    __tablename__ = "allocation"
    specimen_id = db.Column(db.String(), primary_key=True)
    project_id = db.Column(db.String(), primary_key=True)
    is_primary = db.Column(db.String(), nullable=False)
