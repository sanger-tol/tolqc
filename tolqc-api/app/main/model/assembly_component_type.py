# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from tol.api_base.model import Base, db, setup_model


@setup_model
class AssemblyComponentType(Base):
    __tablename__ = 'assembly_component_type'

    class Meta:
        type_ = 'component_types'
        id_column = 'component_type_id'

    component_type_id = db.Column(db.String(), primary_key=True)
    description = db.Column(db.String())

    assemblies = db.relationship('Assembly', back_populates='component_type')
