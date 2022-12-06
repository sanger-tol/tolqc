# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from tol.api_base.model import EnumBase, db, setup_model


@setup_model
class TolqcSex(EnumBase):
    __tablename__ = 'sex'

    class Meta:
        type_ = 'sexes'

    specimen = db.relationship('TolqcSpecimen', back_populates='sex')
