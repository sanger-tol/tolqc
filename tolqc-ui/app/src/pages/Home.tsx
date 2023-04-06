/*
SPDX-FileCopyrightText: 2022 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import AutoTable from "../table/AutoTable";
import { CentreContents } from "@tol/tol-ui"


function Home() {
  return (
    <div className="home">
      <CentreContents>
        <AutoTable 
          endpoint="species"
          fields={{
            "created_at": {},
            "name": {},
            "taxon_id": {
              filterType: 'EXACT'
            }
          }}
        />
        <AutoTable
          endpoint="species"
          fields={{
            "creator.name": {
              rename: "x123"
            },
            "hierarchy_name": {
              rename: "Project",
              width: 600,
              link: "common_name",
              sort: false
            },
            "name": {
              filterType: 'EXACT'
            },
            "common_name": {
              rename: "Common Name",
              filterType: 'EXACT'
            },
            "taxon_id": {
              rename: "Taxon ID"
            },
            "taxon_family": {
              rename: "Family"
            },
            "taxon_order": {
              rename: "Order"
            },
            "taxon_phylum": {
              rename: "Phylum"
            }
          }}
          fixedFilter={{
            "exact": {
              "taxon_family": "Inachidae"
            }
          }}
        />
        <AutoTable endpoint="species" />
      </CentreContents>
    </div>
  );
}

export default Home;
