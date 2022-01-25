# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .creation_log_base import CreationLogBase, db
from .base import setup_model


@setup_model
class TolqcCobiont(CreationLogBase):
    __tablename__ = "cobionts"
    id = db.Column(db.Integer(), primary_key=True)
    cobiont_id = db.Column(db.Integer(), nullable=False)
    name = db.Column(db.String())
    alias = db.Column(db.String())
    specimen_instance_id = db.Column(db.Integer(), db.ForeignKey("specimens.id"),
                                     nullable=False)
    changed = db.Column(db.DateTime())
    current = db.Column(db.String())
    specimens = db.relationship("TolqcSpecimen", back_populates="cobionts",
                                foreign_keys=[specimen_instance_id])
