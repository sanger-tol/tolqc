/*
SPDX-FileCopyrightText: 2022 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import { AutoTable, CentreContents } from '@tol/tol-ui'

function Home() {
  return (
    <div className="home">
      <CentreContents>
        <AutoTable endpoint="data"
          fields={{
            'name': {
              'rename': 'Run/element/tag'
            },
            'runs.start_date': {
              'rename': 'Run'
            },
            'samples.name': {
              'rename': 'Sanger Sample ID'
            },
            'samples.specimens.species.name': {
              'rename': 'Species'
            }
          }}
        />
      </CentreContents>

    </div>
  );
}

export default Home;
