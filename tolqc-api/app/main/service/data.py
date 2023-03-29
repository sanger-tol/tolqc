# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import (
    Accession, AccessionTypeDict, Data, Run, Sample, Species, Specimen
)
from main.schema import DataSchema

from tol.api_base.error import CandidateKeyNotProvidedExpection
from tol.api_base.service import BaseService, provide_body_data, setup_service


@setup_service
class DataService(BaseService):
    class Meta:
        model = Data
        schema = DataSchema
