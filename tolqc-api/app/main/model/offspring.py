# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from tol.api_base.model import Base, db, setup_model


@setup_model
class Offspring(Base):
    __tablename__ = 'offspring'

    class Meta:
        type_ = 'offspring'

    id = db.Column(db.Integer(), primary_key=True)  # noqa: A003
    specimen_id = db.Column(db.String(), db.ForeignKey('specimen.specimen_id'))
    offspring_specimen_id = db.Column(
        db.String(), db.ForeignKey('specimen.specimen_id')
    )

    db.UniqueConstraint('specimen_id', 'offspring_specimen_id')

    parent = db.relationship(
        'Specimen',
        foreign_keys=[specimen_id],
        back_populates='parent_assn',
    )
    offspring = db.relationship(
        'Specimen',
        foreign_keys=[offspring_specimen_id],
        back_populates='offspring_assn',
    )
