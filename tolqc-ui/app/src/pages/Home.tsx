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
      <AutoTable endpoint="species"/>
      <AutoTable endpoint="species"
          fields={{
            'creator.name': {
              rename: 'x123',
              link: 'hello'
            },
            'hierarchy_name': {
              rename: 'Project',
              width: 600,
              link: 'common_name'
            },
            'name': {},
            'common_name': {
              rename: 'Common Name'
            },
            'taxon_id': {
              rename: 'Taxon ID'
            },
            'taxon_family': {
              rename: 'Family'
            },
            'taxon_order': {
              rename: 'Order'
            },
            'taxon_phylum': {
              rename: 'Phylum'
            }
          }}
        />
      </CentreContents>
    </div>
  );
}

export default Home;
