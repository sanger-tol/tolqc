# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .creation_log_base import CreationLogBase, db


class TolqcFile(CreationLogBase):
    __tablename__ = "file"
    id = db.Column(db.Integer(), primary_key=True)
    seq_id = db.Column(db.Integer(), db.ForeignKey("seq.id"))
    name = db.Column(db.String())
    type = db.Column(db.String())
    md5 = db.Column(db.String())
    seq = db.relationship("TolqcSeq", back_populates="file",
                          foreign_keys=[seq_id])
