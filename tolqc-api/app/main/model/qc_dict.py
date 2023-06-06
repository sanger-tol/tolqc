# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from tol.api_base.model import EnumBase, db, setup_model


@setup_model
class QcDict(EnumBase):
    __tablename__ = 'qc_dict'

    class Meta:
        type_ = 'qc_types'

    status = db.relationship('Status', back_populates='qc_dict')
    genomescope_metrics = db.relationship(
        'GenomescopeMetrics', back_populates='qc_dict'
    )
