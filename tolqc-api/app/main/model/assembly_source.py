# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from tol.api_base.model import Base, db, setup_model


@setup_model
class AssemblySource(Base):
    __tablename__ = 'assembly_source'

    class Meta:
        type_ = 'assembly_sources'

    id = db.Column(db.Integer(), primary_key=True)  # noqa: A003
    assembly_id = db.Column(db.Integer(), db.ForeignKey('assembly.assembly_id'))
    source_assembly_id = db.Column(db.Integer(), db.ForeignKey('assembly.assembly_id'))

    db.UniqueConstraint('assembly_id', 'source_assembly_id')

    source = db.relationship(
        'Assembly',
        foreign_keys=[source_assembly_id],
        back_populates='component_assembly_assn',
    )
    component = db.relationship(
        'Assembly',
        foreign_keys=[assembly_id],
        back_populates='source_assembly_assn',
    )
