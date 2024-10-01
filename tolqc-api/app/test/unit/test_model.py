# SPDX-FileCopyrightText: 2024 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from tolqc.flask import models_list
from tolqc.schema.assembly_models import Assembly
from tolqc.schema.folder_models import FolderLocation
from tolqc.schema.sample_data_models import Data
from tolqc.schema.system_models import Token


def test_models_list():
    """ Check that the models_list() is correctly constructed """
    models = models_list()
    assert Assembly in models
    assert Data in models
    assert 'EditData' in [x.__name__ for x in models]
    assert FolderLocation in models
    assert Token not in models
    assert None not in models
