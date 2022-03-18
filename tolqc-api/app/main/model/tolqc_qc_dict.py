# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import db, EnumBase, setup_model


@setup_model
class TolqcQcDict(EnumBase):
    __tablename__ = "qc_dict"

    class Meta:
        type_ = 'qc_types'

    status = db.relationship("TolqcStatus", back_populates="qc_dict")
    genomescope_metrics = db.relationship("TolqcGenomescopeMetrics",
                                          back_populates="qc_dict")
