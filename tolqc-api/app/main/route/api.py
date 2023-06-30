# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask import Blueprint

from flask_restx import Api

from main.resource import (
    api_accession,
    api_accession_type_dict,
    api_allocation,
    api_assembly,
    api_assembly_component_type,
    api_assembly_metrics,
    api_assembly_source,
    api_assembly_status,
    api_assembly_status_type,
    api_barcode_metrics,
    api_busco_lineage,
    api_busco_metrics,
    api_centre,
    api_contigviz_metrics,
    api_data,
    api_dataset,
    api_dataset_element,
    api_dataset_status,
    api_dataset_status_type,
    api_file,
    api_genomescope_metrics,
    api_library,
    api_library_type,
    api_markerscan_metrics,
    api_merqury_metrics,
    api_offspring,
    api_pacbio_run_metrics,
    api_platform,
    api_ploidyplot_metrics,
    api_project,
    api_qc_dict,
    api_review_dict,
    api_run,
    api_sample,
    api_sex,
    api_software_version,
    api_species,
    api_specimen,
    api_specimen_status,
    api_specimen_status_type,
)


from tol.api_base.auth import authorizations
from tol.api_base.resource import api_auth, api_environment, api_user


def _get_environment_string(app):
    environment = app.config['DEPLOYMENT_ENVIRONMENT']
    if environment == 'production':
        return ''
    return f' ({environment})'


def _setup_api(blueprint, app):
    api = Api(
        blueprint,
        doc='/ui',
        title=f'Tree of Life Quality Control{_get_environment_string(app)}',
        authorizations=authorizations,
    )
    api.add_namespace(api_accession)
    api.add_namespace(api_accession_type_dict)
    api.add_namespace(api_allocation)
    api.add_namespace(api_assembly)
    api.add_namespace(api_assembly_component_type)
    api.add_namespace(api_assembly_metrics)
    api.add_namespace(api_assembly_source)
    api.add_namespace(api_assembly_status)
    api.add_namespace(api_assembly_status_type)
    api.add_namespace(api_auth)
    api.add_namespace(api_barcode_metrics)
    api.add_namespace(api_busco_lineage)
    api.add_namespace(api_busco_metrics)
    api.add_namespace(api_centre)
    api.add_namespace(api_contigviz_metrics)
    api.add_namespace(api_data)
    api.add_namespace(api_dataset)
    api.add_namespace(api_dataset_element)
    api.add_namespace(api_dataset_status)
    api.add_namespace(api_dataset_status_type)
    api.add_namespace(api_environment)
    api.add_namespace(api_file)
    api.add_namespace(api_genomescope_metrics)
    api.add_namespace(api_library)
    api.add_namespace(api_library_type)
    api.add_namespace(api_markerscan_metrics)
    api.add_namespace(api_merqury_metrics)
    api.add_namespace(api_offspring)
    api.add_namespace(api_pacbio_run_metrics)
    api.add_namespace(api_platform)
    api.add_namespace(api_ploidyplot_metrics)
    api.add_namespace(api_project)
    api.add_namespace(api_qc_dict)
    api.add_namespace(api_review_dict)
    api.add_namespace(api_run)
    api.add_namespace(api_sample)
    api.add_namespace(api_sex)
    api.add_namespace(api_software_version)
    api.add_namespace(api_species)
    api.add_namespace(api_specimen)
    api.add_namespace(api_specimen_status)
    api.add_namespace(api_specimen_status_type)
    api.add_namespace(api_user)


def init_blueprints(app):
    blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
    _setup_api(blueprint, app)
    return blueprint
