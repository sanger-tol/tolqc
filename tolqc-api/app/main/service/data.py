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

    @classmethod
    @provide_body_data
    def register(cls, data):
        # TODO:
        # schema validation
        try:
            # sample_ref: sample.name
            # public_name: specimen.name
            # common_name: species.name
            # supplier_name: specimen.supplied_name (STS: specimen_id)
            # accession_number: sample.accession.name (STS: biosample)
            # donor_id: specimen.accession.name (STS: biospecimen)
            # taxon_id: species.taxon_id
            # instrument_model: run.platform.model
            # run_id: run.name
            # start_date: run.start_date NEW
            # qc_date: run.qc_date NEW
            # position: run.element
            # tag: data.tag_index
            # pipeline_id_lims, # lookup/enum: platform/library (may be another MLWH column)
            # tag_sequence: data.tag1_id
            # tag2_sequence: data.tag2_id
            # complete_date: run.date
            # study_id: project.lims_id
            # study_name: project.name
            # manual_qc: data.lims_qc

            # Species
            species_data = {'name': data.get('common_name'),
                            'taxon_id': data.get('taxon_id')}
            species, new = Species.one_or_create(
                {
                    'id': species_data.get('taxon_id')
                },
                data=species_data
            )
            if new:
                species.add()

            # Accession type
            accession_data = {'name': 'biospecimen'}
            accession_type, new = AccessionTypeDict.one_or_create(
                {
                    'name': accession_data.get('name')
                },
                data=accession_data
            )
            if new:
                accession_type.add()

            # Accession
            accession_data = {'name': data.get('donor_id')}
            accession, new = Accession.one_or_create(
                {
                    'id': species_data.get('supplier_name')
                },
                data=accession_data
            )
            if new:
                accession.accession_type = accession_type
                accession.add()

            # Specimen
            specimen_data = {'name': data.get('public_name'),
                             'supplier_name': data.get('supplied_name')}
            specimen, new = Specimen.one_or_create(
                {
                    'id': species_data.get('supplier_name')
                },
                data=specimen_data
            )
            if new:
                specimen.species = species
                specimen.accession = accession
                specimen.add()

            # Accession type
            accession_data = {'name': 'biosample'}
            accession_type, new = AccessionTypeDict.one_or_create(
                {
                    'name': accession_data.get('name')
                },
                data=accession_data
            )
            if new:
                accession_type.add()

            # Accession
            accession_data = {'name': data.get('accession_number')}
            accession, new = Accession.one_or_create(
                {
                    'id': accession_data.get('name')
                },
                data=accession_data
            )
            if new:
                accession.accession_type = accession_type
                accession.add()

            # Sample
            sample_data = {'name': data.get('sample_ref')}
            sample, new = Sample.one_or_create(
                {
                    'name': sample_data.get('name')
                },
                data=sample_data
            )
            if new:
                sample.specimen = specimen
                sample.accession = accession
                sample.add()

            # Run
            run_data = {'name': data.get('run_id'),
                        'position': data.get('position'),
                        'start_date': data.get('start_date'),
                        'qc_date': data.get('qc_date'),
                        'complete_date': data.get('complete_date')}

            run, new = Run.one_or_create(
                {
                    'name': run_data.get('name')
                },
                data=run_data
            )
            if new:
                run.add()

            # Data
            data_data = {'tag_index': data.get('tag'),
                         'tag1_id': data.get('tag_sequence'),
                         'tag2_id': data.get('tag2_sequence'),
                         'lims_qc': data.get('lims_qc')}

            data, new = Data.one_or_create(
                {
                    'run_instance_id': data.get('run_id'),
                    'tag_index': data.get('tag_index')
                },
                data=data_data
            )
            if new:
                data.run = run
                data.add()

        except CandidateKeyNotProvidedExpection as error:
            return {
                'error': {
                    'title': 'Bad Request',
                    'code': 400,
                    'detail': str(error)
                }
            }, 400

        return {
            'data': {
                'type': 'datas',
                'id': data.id
            }
        }, 201
