# SPDX-FileCopyrightText: 2024 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import json
from datetime import datetime

from tolqc.model import EditBase
from tolqc.sample_data_models import Data, Species

from .conftest import SKIP_IF_NO_DB_URI_ENV as pytestmark  # noqa: F401, N811


def test_modify_species(logbase_db_session):
    """
    Tests modification of a LogBase class, recording changes of String,
    Integer and None values.
    """
    spkld = Species(
        species_id='Pararge aegeria',
        hierarchy_name='Pararge_aegeria',
        strain=None,
        common_name='speckled wood',
        taxon_id=116150,
        taxon_family='Nymphalidae',
        taxon_order='Lepidoptera',
        taxon_phylum='Arthropoda',
        taxon_group='insects',
        genome_size=479220000,
        chromosome_number=54,
    )
    logbase_db_session.add(spkld)
    logbase_db_session.flush()

    # Test that modified_at and modified_by get filled in
    first_save = spkld.modified_at
    assert isinstance(first_save, datetime)
    assert spkld.modified_by is not None

    # Change to the "tircis" subspecies
    spkld.strain = 'tircis'
    spkld.taxon_id = 348721
    logbase_db_session.flush()

    # The edit should now appear in the history
    spkld_edit = spkld.edit_history[0]
    assert isinstance(spkld_edit, EditBase)

    # The edit's modified_at is the original species row's value
    assert spkld_edit.modified_at == first_save

    # Same user, so modified_by should match
    assert spkld_edit.modified_by == spkld.modified_by

    # The species' modified_at entry should be more recent
    assert spkld_edit.modified_at < spkld.modified_at

    # Edit contains the original value of the columns
    assert json.loads(spkld_edit.changes) == {
        'strain': None,
        'taxon_id': 116150,
    }


def test_modify_data(logbase_db_session):
    """
    Tests recording changes in datetime values, and sorting of history by most
    recent first.
    """
    date1 = datetime.fromisoformat('2023-07-14T11:12:02+01:00')
    date2 = datetime.fromisoformat('2023-08-21T13:44:04+01:00')
    date3 = datetime.fromisoformat('2023-08-22T10:32:06+01:00')
    dat = Data(
        name_root='test',
        lims_qc='pass',
        date=date1,
    )
    logbase_db_session.add(dat)
    logbase_db_session.flush()

    # lims_qc changed to fail on second date
    dat.lims_qc = 'fail'
    dat.date = date2
    logbase_db_session.flush()

    # lims_qc changed back to pass on third date
    dat.lims_qc = 'pass'
    dat.date = date3
    logbase_db_session.flush()

    # Should now have two entries in the edit history
    hist = dat.edit_history
    assert len(hist) == 2

    # Check sort order of change history is most recent first
    assert hist[0].modified_at > hist[1].modified_at

    # Check history entries for date and string are as expected
    edit2, edit1 = (json.loads(h.changes) for h in hist)
    assert len(edit1) == 2  # Check that we only have two
    assert len(edit2) == 2  # keys in each changes dict.
    assert edit1['lims_qc'] == 'pass'
    assert edit2['lims_qc'] == 'fail'
    assert datetime.fromisoformat(edit1['date']) == date1
    assert datetime.fromisoformat(edit2['date']) == date2
