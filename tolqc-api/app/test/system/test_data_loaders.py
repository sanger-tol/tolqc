# SPDX-FileCopyrightText: 2024 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import json

import pytest

from sqlalchemy import text

from tolqc.marshal.seq_data import (
    accession_if_valid,
    build_data,
    build_files,
    build_library,
    build_library_type,
    build_sample,
    get_centre,
    maybe_datetime,
    parse_ndjson_row,
    row_message,
    valid_accession,
)
from tolqc.sample_data_models import (
    Accession,
    Centre,
    Data,
    File,
    Library,
    LibraryType,
    Sample,
)


from .conftest import SKIP_IF_NO_DB_URI_ENV as pytestmark  # noqa: F401, N811


def test_row_message():
    expected = ''.join(
        (
            'Bad row:\n',
            '        n = 10\n',
            '  missing = \n',
            '  present = val\n',
        )
    )
    assert (
        row_message(
            {
                'n': 10,
                'missing': None,
                'present': 'val',
            },
            'Bad row',
        )
        == expected
    )


def test_tz_is_europe_london(db_session):
    """
    Check that the database server is set to the expected time
    zone 'Europe/London'
    """
    tz, = db_session.execute(text('SHOW timezone')).one()
    assert tz == 'Europe/London'


def test_valid_accession(db_session):
    acc_type = 'Bio Sample'

    good = 'SAMXX0001'
    assert valid_accession(db_session, acc_type, good)
    assert isinstance(accession_if_valid(db_session, acc_type, good), Accession)

    bad = 'SAMXXX001'
    assert not valid_accession(db_session, acc_type, bad)
    assert accession_if_valid(db_session, acc_type, bad) is None


def test_build_file():
    (file1,) = build_files({'irods_path': '/seq/data', 'irods_file': 'd.cram'})
    assert isinstance(file1, File)
    assert file1.remote_path == 'irods:/seq/data/d.cram'
    (file2,) = build_files({'irods_path': '/seq/data/', 'irods_file': 'd.cram'})
    assert file1.remote_path == file2.remote_path
    assert build_files({'irods_path': None}) is None
    with pytest.raises(ValueError):
        build_files({'irods_path': '/seq/data', 'irods_file': None})


def test_build_library(db_session):
    lib_id = 'x1'
    lib1 = build_library(
        db_session,
        {
            'library_id': lib_id,
            'pipeline_id_lims': 'Pacbio_IsoSeq',
        },
    )
    assert isinstance(lib1, Library)
    assert isinstance(lib1.library_type, LibraryType)
    db_session.add(lib1)
    lib2 = build_library(
        db_session,
        {
            'library_id': lib_id,
            'pipeline_id_lims': None,
        },
    )
    assert lib2 is lib1
    assert lib2.library_type.library_type_id == 'PacBio - IsoSeq'
    assert build_library_type(db_session, {'pipeline_id_lims': None}) is None


def test_build_sample_specimen_species(db_session):
    row = {
        'sample_name': 'JTOL1001',
        'scientific_name': "Tyrnanosaurus rex 'Jurassic Park 1993'",
        'supplier_name': 'JRSPK1993',
        'tol_specimen_id': 'rTyrRex1',
        'biospecimen_accession': None,
        'biosample_accession': None,
        'taxon_id': None,
    }
    smpl = build_sample(db_session, row)
    db_session.add(smpl)
    assert isinstance(smpl, Sample)
    assert (
        smpl.specimen.species.hierarchy_name == 'Tyrnanosaurus_rex_Jurassic_Park_1993'
    )


def test_build_data(db_session, row_data):
    centre = get_centre(db_session, 'Wellcome Sanger Institute')
    assert isinstance(centre, Centre)

    with db_session.no_autoflush:
        p_data = build_data(db_session, centre, row_data['pacbio'])
        db_session.add(p_data)
        db_session.flush()

    assert isinstance(p_data, Data)
    assert p_data.run.plex_count == 4
    assert p_data.run.platform.name == 'PacBio'
    assert p_data.visibility == 'Always'
    assert len(p_data.projects) == 1
    assert p_data.sample.accession
    assert p_data.sample.specimen.accession
    assert p_data.run.pacbio_run_metrics
    assert p_data.sample.accession.accession_id == 'SAMEA112468058'
    assert p_data.sample.specimen.accession.accession_id == 'SAMEA112468032'
    assert p_data.sample.specimen.species

    with db_session.no_autoflush:
        i_data = build_data(db_session, centre, row_data['illumina'])
        db_session.add(i_data)
        db_session.flush()

    assert isinstance(i_data, Data)
    assert i_data.run.platform.name == 'Illumina'
    assert i_data.visibility == 'Always'
    assert len(i_data.projects) == 1

    # Illumina data object should connect to these same objects as the PacBio
    # data:
    assert i_data.sample.accession is p_data.sample.accession
    assert i_data.sample.specimen is p_data.sample.specimen
    assert i_data.sample.specimen.species is p_data.sample.specimen.species


def test_fail_mising_name(client, api_path):
    with pytest.raises(ValueError, match=r"Missing 'name'"):
        client.post(api_path + '/loader/seq-data', data='{"study_id":"1001"}')


def test_seq_data_loader(client, api_path, ndjson_row_data):
    response = client.post(api_path + '/loader/seq-data', data=ndjson_row_data)
    assert response.status == '200 OK'
    assert response.json == {
        'new': [
            {
                'name': 'm64221e_230627_234912',
                'specimen': 'bBraLeu2',
                'species': 'Branta leucopsis',
                'library_type': 'PacBio - HiFi',
                'sample': 'DTOL13630432',
                'project': 'DTOL_Darwin Tree of Life',
            },
            {
                'name': '47339_3#7',
                'specimen': 'bBraLeu2',
                'species': 'Branta leucopsis',
                'library_type': 'Hi-C - Arima v2',
                'sample': 'DTOL13633579',
                'project': 'DTOL_Darwin Tree of Life',
            },
        ],
        'updated': [],
    }


def test_seq_data_loader_update(client, api_path, row_data):
    response = client.post(api_path + '/loader/seq-data', data=to_ndjson(row_data))
    row_data['pacbio']['lims_qc'] = 'fail'
    row_data['pacbio']['qc_date'] = '2023-07-02T10:45:00+01:00'
    response = client.post(api_path + '/loader/seq-data', data=to_ndjson(row_data))
    assert response.status == '200 OK'
    assert response.json == {
        'new': [],
        'updated': [
            {
                'name': 'm64221e_230627_234912',
                'specimen': 'bBraLeu2',
                'species': 'Branta leucopsis',
                'library_type': 'PacBio - HiFi',
                'sample': 'DTOL13630432',
                'project': 'DTOL_Darwin Tree of Life',
                'changes': {
                    'lims_qc': ['pass', 'fail'],
                    'date': [
                        '2023-06-30T11:29:00+01:00',
                        '2023-07-02T10:45:00+01:00',
                    ],
                },
            }
        ],
    }


def test_maybe_datetime():
    assert maybe_datetime({}, 'date_x') is None
    dt_str = '1981-09-19T18:30:00-04:00'
    dt = maybe_datetime({'date_x': dt_str}, 'date_x')
    assert dt.isoformat() == dt_str


def test_row_parse():
    too_big = json.dumps({'x': '#' * 100_000})
    with pytest.raises(ValueError):
        parse_ndjson_row(too_big)
    with pytest.raises(ValueError):
        parse_ndjson_row('["ele"]')
    with pytest.raises(ValueError):
        parse_ndjson_row('{"x": ["y"]}')
    assert parse_ndjson_row('{"x": "  "}') == {'x': None}


def to_ndjson(row_dict):
    return ''.join(
        json.dumps(row, separators=(',', ':')) + '\n' for row in row_dict.values()
    )


@pytest.fixture
def ndjson_row_data(row_data):
    return to_ndjson(row_data)


@pytest.fixture
def row_data():
    return {
        'pacbio': {
            'name': 'm64221e_230627_234912',
            'study_id': '5901',
            'sample_name': 'DTOL13630432',
            'supplier_name': 'NHMUK014561636',
            'tol_specimen_id': 'bBraLeu2',
            'biosample_accession': 'SAMEA112468058',
            'biospecimen_accession': 'SAMEA112468032',
            'scientific_name': 'Branta leucopsis',
            'taxon_id': 184711,
            'platform_type': 'PacBio',
            'instrument_model': 'Sequel IIe',
            'instrument_name': 'm64221e',
            'pipeline_id_lims': 'Pacbio_HiFi',
            'run_id': 'm64221e_230627_234912',
            'lims_run_id': 'TRACTION-RUN-642',
            'well_label': 'H1',
            'run_start': '2023-06-19T15:23:28+01:00',
            'run_complete': '2023-06-29T03:57:38+01:00',
            'lims_qc': 'pass',
            'qc_date': '2023-06-30T11:29:00+01:00',
            'plex_count': 4,
            'tag1_id': 'bc2050',
            'tag2_id': None,
            'library_id': 'DTOL13630432',
            'movie_minutes': 1440,
            'binding_kit': 'Sequel II Binding Kit 3.2',
            'sequencing_kit': 'Sequel II Sequencing Plate 2.0 (4 rxn)',
            'include_kinetics': 'false',
            'loading_conc': 94.0,
            'control_num_reads': 2367,
            'control_read_length_mean': 88287,
            'polymerase_read_bases': 487169541261,
            'polymerase_num_reads': 5734530,
            'polymerase_read_length_mean': 84954,
            'polymerase_read_length_n50': 176250,
            'insert_length_mean': 15655,
            'insert_length_n50': 20250,
            'unique_molecular_bases': 80659808256,
            'p0_num': 2046474,
            'p1_num': 5736897,
            'p2_num': 231300,
            'hifi_read_bases': 26909305485,
            'hifi_num_reads': 2458338,
            'hifi_low_quality_num_reads': None,
            'irods_path': '/seq/pacbio/r64221e_20230619_152240/8_H01/',
            'irods_file': 'demultiplex.bc2050--bc2050.bam',
        },
        'illumina': {
            'name': '47339_3#7',
            'study_id': '5901',
            'sample_name': 'DTOL13633579',
            'supplier_name': 'NHMUK014561636',
            'tol_specimen_id': 'bBraLeu2',
            'biosample_accession': 'SAMEA112468058',
            'biospecimen_accession': 'SAMEA112468032',
            'scientific_name': 'Branta leucopsis',
            'taxon_id': 184711,
            'platform_type': 'Illumina',
            'instrument_model': 'NovaSeq',
            'instrument_name': 'NV15',
            'pipeline_id_lims': 'Hi-C - Arima v2',
            'run_id': '47339',
            'position': '3',
            'tag_index': '7',
            'run_complete': '2023-05-25T05:18:51+01:00',
            'lims_qc': 'pass',
            'qc_date': '2023-06-02T11:23:31+01:00',
            'tag1_id': '39',
            'tag2_id': '39',
            'library_id': 'SQPP-21698-M:G5',
            'irods_path': '/seq/illumina/runs/47/47339/lane3/plex7/',
            'irods_file': '47339_3#7.cram',
        },
    }
