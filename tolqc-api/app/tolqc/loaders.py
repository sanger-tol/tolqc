# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask import Blueprint, request

from tol.api_base2 import custom_blueprint

from tolqc.auth import require_registered
from tolqc.marshal.dataset import load_dataset_stream
from tolqc.marshal.seq_data import load_seq_data_stream
from tolqc.marshal.status import load_status_stream


def loaders_blueprint(
    session_factory,
    url_prefix: str = '/loader',
) -> Blueprint:
    ldr = custom_blueprint(name='loader', url_prefix=url_prefix)

    @ldr.route('/seq-data', methods=['POST'])
    @require_registered
    def load_seq_data():
        session = session_factory()
        changes = load_seq_data_stream(session, request.stream)
        session.commit()

        # Report data loaded and updated
        return changes, 200, {'Content-Type': 'application/json'}

    @ldr.route('/dataset', methods=['POST'])
    @require_registered
    def load_datasets():
        session = session_factory()
        results = load_dataset_stream(session, request.stream)
        session.commit()

        # Report data loaded and updated
        return results, 200, {'Content-Type': 'application/json'}

    @ldr.route('/status/<string:table>', methods=['POST'])
    @require_registered
    def load_statuses(table):
        session = session_factory()
        results = load_status_stream(session, request.stream, table)
        session.commit()

        # Report data loaded and updated
        return results, 200, {'Content-Type': 'application/json'}

    return ldr
