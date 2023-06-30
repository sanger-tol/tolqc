# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from tol.api_base.model import Base, db, setup_model


@setup_model
class SpecimenStatusType(Base):
    __tablename__ = 'specimen_status_type'

    class Meta:
        type_ = 'specimen_status_types'
        id_column = 'status_type_id'

    status_type_id = db.Column(db.String(), primary_key=True)
    description = db.Column(db.String())
    assign_order = db.Column(db.Integer())

    statuses = db.relationship('SpecimenStatus', back_populates='status_type')
