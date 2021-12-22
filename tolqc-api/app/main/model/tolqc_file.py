# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .sub_base import SubBase, db


class TolqcFile(SubBase):
    __tablename__ = "file"
    id = db.Column(db.Integer(), primary_key=True)
    file_id = db.Column(db.String())
    seq_instance_id = db.Column(db.Integer(), db.ForeignKey("seq.id"),
                                nullable=False)
    name = db.Column(db.String())
    type = db.Column(db.String())
    md5 = db.Column(db.String())
    changed = db.Column(db.DateTime())
    current = db.Column(db.Boolean())
    seq = db.relationship("TolqcSeq", back_populates="file",
                              foreign_keys=[seq_instance_id])
