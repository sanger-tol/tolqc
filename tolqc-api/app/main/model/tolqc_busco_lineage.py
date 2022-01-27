# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .creation_log_base import CreationLogBase, db


class TolqcBuscoLineage(CreationLogBase):
    __tablename__ = "busco_lineage"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    date_created = db.Column(db.DateTime())
    species_count = db.Column(db.Integer())
    gene_count = db.Column(db.Integer())
    busco_metrics = db.relationship("TolqcBuscoMetrics", back_populates="busco_lineage")
