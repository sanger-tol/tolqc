/*
SPDX-FileCopyrightText: 2022 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import { RemoteTable, Widgets, Button, Row, Col, useZone } from "@tol/tol-ui";
import { TOLQC_DS } from "..";

const button = (
  <Button
  text="Visit ToL Portal"
  onClick={() => window.open("https://portal.tol.sanger.ac.uk", "_blank")}
/>
);

const title = (
  <span>
    <p className="mt-2">
      Welcome to ToLQC. This is the admin interface for the ToLQC process. To view data, please
      visit the ToL Portal.
    </p>
  </span>
);

const intro = (
  <Row>
    <Col xs={12} sm={8}>
      {title}
    </Col>
    <Col xs={12} sm={4}>
      {button}
    </Col>
  </Row>
);

function Home() {

  const tolQCTable = useZone({
    objectType: "data",
    dataSource: TOLQC_DS,
    components: [{ id: "home-table" }],
  });

  const dataTable = (
    <RemoteTable
      height={500}
      fields={{
        data: {
          id: {
            rename: "ID",
          },
          date: {
            rename: "Date",
          },
          name: {
            rename: "Name",
          },
          "sample.id": {
            rename: "Sanger Sample ID",
          },
        },
        order: {
          active: ["id", "date", "sample.id"],
        },
      }}
      {...tolQCTable}
    />
  );

  const Components = [
    {
      component: intro,
      type: "full",
    },
    {
      component: dataTable,
      type: "full",
    },
  ];

  return (
    <div className="data">
      <Widgets components={Components} />
    </div>
  );
}
export default Home;
