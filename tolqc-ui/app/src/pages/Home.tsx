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
          requiredFields={{
            'hierarchy_name': 'Project',
            'name': 'Name',
            'common_name': 'Common name',
            'taxon_id': "Taxon ID",
            'taxon_family': 'Family',
            'taxon_order': 'Order',
            'taxon_phylum': 'Phylum'
          }}
        />
      </CentreContents>
    </div>
  );
}

export default Home;