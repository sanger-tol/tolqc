# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .log_base import LogBase, db
from .base import setup_model


@setup_model
class TolqcFile(LogBase):
    __tablename__ = "files"
    id = db.Column(db.Integer(), primary_key=True)
    file_id = db.Column(db.String())
    seq_instance_id = db.Column(db.Integer(), db.ForeignKey("seq.id"),
                                nullable=False)
    name = db.Column(db.String())
    type = db.Column(db.String())
    md5 = db.Column(db.String())
    changed = db.Column(db.DateTime())
    current = db.Column(db.Boolean())
    seq = db.relationship("TolqcSeq", back_populates="files",
                          foreign_keys=[seq_instance_id])
