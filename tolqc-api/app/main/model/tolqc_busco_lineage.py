# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .log_base import LogBase, db
from .base import setup_model


@setup_model
class TolqcBuscoLineage(LogBase):
    __tablename__ = "busco_lineage"

    class Meta:
        type_ = 'busco_lineages'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    date_created = db.Column(db.DateTime())
    species_count = db.Column(db.Integer())
    gene_count = db.Column(db.Integer())
    busco_metrics = db.relationship("TolqcBuscoMetrics", back_populates="busco_lineage")
