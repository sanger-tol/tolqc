# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from tol.api_base.model import Base, db, setup_model


@setup_model
class BuscoLineage(Base):
    __tablename__ = 'busco_lineage'

    class Meta:
        type_ = 'busco_lineages'

    id = db.Column(db.Integer(), primary_key=True)  # noqa: A003
    name = db.Column(db.String())
    date_created = db.Column(db.DateTime())
    species_count = db.Column(db.Integer())
    gene_count = db.Column(db.Integer())
    busco_metrics = db.relationship(
        'BuscoMetrics', back_populates='busco_lineage'
    )
