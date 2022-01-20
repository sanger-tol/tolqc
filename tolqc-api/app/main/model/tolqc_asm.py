# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .sub_base import SubBase, db


class TolqcAsm(SubBase):
    __tablename__ = "asm"
    id = db.Column(db.Integer(), primary_key=True)
    data_instance_id = db.Column(db.Integer(), db.ForeignKey("data.id"),
                                 nullable=False)
    name = db.Column(db.String())
    description = db.Column(db.String())
    asm_stats_instance_id = db.Column(db.Integer(), db.ForeignKey("asm_stats.id"),
                                      nullable=False)
    data = db.relationship("TolqcData", back_populates="asm",
                           foreign_keys=[data_instance_id])
    asm_stats = db.relationship("TolqcAsmStats", back_populates="asm",
                                foreign_keys=[asm_stats_instance_id])
