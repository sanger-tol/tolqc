# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import os

from flask import Flask
from tol.api_base2 import data_blueprint
from tol.api_base2.misc import quick_and_dirty_auth
from tol.core import core_data_object
from tol.sql import create_sql_datasource
from tolqc.model import (
    Accession,
    AccessionTypeDict,
    Allocation,
    Assembly,
    AssemblyComponentType,
    AssemblyMetrics,
    AssemblySource,
    AssemblyStatus,
    AssemblyStatusType,
    BarcodeMetrics,
    BuscoLineage,
    BuscoMetrics,
    Centre,
    ContigvizMetrics,
    Data,
    Dataset,
    DatasetElement,
    DatasetStatus,
    DatasetStatusType,
    File,
    GenomescopeMetrics,
    Library,
    LibraryType,
    MarkerscanMetrics,
    MerquryMetrics,
    Offspring,
    PacbioRunMetrics,
    Platform,
    PloidyplotMetrics,
    Project,
    QCDict,
    ReviewDict,
    Run,
    Sample,
    Sex,
    SoftwareVersion,
    Species,
    Specimen,
    SpecimenStatus,
    SpecimenStatusType,
)


def application():
    app = Flask(__name__)

    # Tol QC endpoints
    tolqc = create_sql_datasource(
        models=[
            Accession,
            AccessionTypeDict,
            Allocation,
            Assembly,
            AssemblyComponentType,
            AssemblyMetrics,
            AssemblySource,
            AssemblyStatus,
            AssemblyStatusType,
            BarcodeMetrics,
            BuscoLineage,
            BuscoMetrics,
            Centre,
            ContigvizMetrics,
            Data,
            Dataset,
            DatasetElement,
            DatasetStatus,
            DatasetStatusType,
            File,
            GenomescopeMetrics,
            Library,
            LibraryType,
            MarkerscanMetrics,
            MerquryMetrics,
            Offspring,
            PacbioRunMetrics,
            Platform,
            PloidyplotMetrics,
            Project,
            QCDict,
            ReviewDict,
            Run,
            Sample,
            Sex,
            SoftwareVersion,
            Species,
            Specimen,
            SpecimenStatus,
            SpecimenStatusType,
        ],
        db_uri=os.getenv('DB_URI'),
    )
    authenticator = quick_and_dirty_auth(omnipotent_token='needToKnow43957')
    blueprint_data_tolqc = data_blueprint(tolqc, authenticator=authenticator)
    app.register_blueprint(
        blueprint_data_tolqc,
        name='tolqc',
        url_prefix='/tolqc',
    )

    core_data_object(tolqc)

    return app
