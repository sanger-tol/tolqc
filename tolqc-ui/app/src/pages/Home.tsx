/*
SPDX-FileCopyrightText: 2022 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import { RemoteTable, Widgets, Button, Row, Col} from '@tol/tol-ui'

const button = (
	<Button
		href="https://portal.tol.sanger.ac.uk"
		style={{float: "right"}}
	>
		Visit ToL Portal
	</Button>
)

const title = (
	<span>
		<p className='mt-2'>
			Welcome to ToLQC. The preferred place to view ToLQC data is in the ToL Portal.
		</p>
	</span>
)

const intro = (
	<Row>
		<Col xs={12} sm={8}>{title}</Col>
		<Col xs={12} sm={4}>{button}</Col>
	</Row>
)

const dataTable = (
  <RemoteTable
		id="data-home-table-v2"
    endpoint="data"
    height={500}
    fields={{
      "id": {
        rename: "ID"
      },
      "date": {
        rename: "Date"
      },
      "name": {
        rename: "Name"
      },
      "sample.id": {
        rename: "Sanger Sample ID",
        relationshipBox: true
      }
    }}
  />
)



function Home() {
  return (
    <div className="data">
      <Widgets components={[intro]}/>
      <Widgets components={[
				dataTable
			]}/>
    </div>
  );
}
export default Home;
