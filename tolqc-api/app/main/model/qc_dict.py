# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from tol.api_base.model import Base, db, setup_model


@setup_model
class QCDict(Base):
    __tablename__ = 'qc_dict'

    class Meta:
        type_ = 'qc_dict'
        id_column = 'qc_state'

    qc_state = db.Column(db.String(), primary_key=True)
