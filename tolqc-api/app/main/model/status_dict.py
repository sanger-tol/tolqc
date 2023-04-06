# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from tol.api_base.model import EnumBase, db, setup_model


@setup_model
class StatusDict(EnumBase):
    __tablename__ = 'status_dict'

    class Meta:
        type_ = 'status_types'

    status = db.relationship('Status', back_populates='status_dict')
