# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask import Blueprint
from flask_restx import Api

from main.auth import authorizations
from main.resource import api_centre, api_environment, \
                          api_user, api_run, api_specimen, \
                          api_species, api_seq, api_sample, \
                          api_project, api_platform, api_library, \
                          api_library_type, api_allocation, \
                          api_data, api_file, \
                          api_seq_data, api_sex, \
                          api_software_version, api_status


def _get_environment_string(app):
    environment = app.config['DEPLOYMENT_ENVIRONMENT']
    if environment == 'production':
        return ""
    return f" ({environment})"


def _setup_api(blueprint, app):
    api = Api(
        blueprint,
        doc='/ui',
        title=f"Tree of Life Quality Control{_get_environment_string(app)}",
        authorizations=authorizations
    )
    api.add_namespace(api_centre)
    api.add_namespace(api_user)
    api.add_namespace(api_run)
    api.add_namespace(api_environment)
    api.add_namespace(api_specimen)
    api.add_namespace(api_species)
    api.add_namespace(api_seq)
    api.add_namespace(api_sample)
    api.add_namespace(api_project)
    api.add_namespace(api_platform)
    api.add_namespace(api_library)
    api.add_namespace(api_library_type)
    api.add_namespace(api_allocation)
    api.add_namespace(api_data)
    api.add_namespace(api_file)
    api.add_namespace(api_seq_data)
    api.add_namespace(api_sex)
    api.add_namespace(api_software_version)
    api.add_namespace(api_status)


def init_blueprint(app):
    blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
    _setup_api(blueprint, app)
    return blueprint
