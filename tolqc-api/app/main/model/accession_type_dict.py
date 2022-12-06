# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from tol.api_base.model import EnumBase, db, setup_model


@setup_model
class TolqcAccessionTypeDict(EnumBase):
    __tablename__ = 'accession_type_dict'

    class Meta:
        type_ = 'accession_types'

    accession = db.relationship('TolqcAccession', back_populates='accession_type_dict')
