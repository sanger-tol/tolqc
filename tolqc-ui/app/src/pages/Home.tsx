/*
SPDX-FileCopyrightText: 2022 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import AutoTable from "../table/AutoTable";
import { CentreContents } from '@tol/tol-ui'

function Home() {
  return (
    <div className="home">
      <CentreContents>
      <AutoTable endpoint="species"
          fields={{
            'hierarchy_name': {
              name: 'Project'
            },
            'name': {},
            'common_name': {
              name: 'Common name'
            },
            'taxon_id': {
              name: 'Taxon ID'
            },
            'taxon_family': {
              name: 'Family'
            },
            'taxon_order': {
              name: 'Order'
            },
            'taxon_phylum': {
              name: 'Phylum'
            }
          }}
        />
      </CentreContents>
    </div>
  );
}

export default Home;
