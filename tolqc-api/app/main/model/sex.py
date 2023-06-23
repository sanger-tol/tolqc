# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from tol.api_base.model import Base, db, setup_model


@setup_model
class Sex(Base):
    __tablename__ = 'sex'

    class Meta:
        type_ = 'sexes'
        id_column = 'sex_id'

    sex_id = db.Column(db.String(), primary_key=True)
    description = db.Column(db.String())

    specimens = db.relationship('Specimen', back_populates='sex')
