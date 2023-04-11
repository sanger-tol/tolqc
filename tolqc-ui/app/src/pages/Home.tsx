/*
SPDX-FileCopyrightText: 2022 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import { AutoTable, CentreContents } from '@tol/tol-ui'

function Home() {
  return (
    <div className="home">
      <CentreContents>
        <AutoTable endpoint="species"
          fields={{
            'hierarchy_name': {
              'rename': 'Project'
            },
            'name': {},
            'common_name': {},
            'taxon_id': {
              'rename': 'Taxon ID'
            },
            'taxon_family': {
              'rename': 'Family'
            },
            'taxon_order': {
              'rename': 'Order'
            },
            'taxon_phylum': {
              'rename': 'Phylum'
            }
          }}
        />
      </CentreContents>

    </div>
  );
}

export default Home;
