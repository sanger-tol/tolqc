/*
SPDX-FileCopyrightText: 2021 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import React from "react";
import { Container, Row, Col } from "react-bootstrap"; 
import { Link } from "react-router-dom";

function Home() {
  return (
    <div className="home">
      <header className="masthead text-center text-white">
        <div className="masthead-content">
          <Container>
            <h1 className="masthead-heading mb-0">ToLQC</h1>
            <h2 className="masthead-subheading mb-0">Tree of Life QC</h2>
            <a href="api/v1/ui" className="btn btn-primary btn-xl rounded-pill mt-5">Use the API</a>
            <a href="https://tolqc.cog.sanger.ac.uk" className="btn btn-primary btn-xl rounded-pill mt-5">View the UI</a>
          </Container>
        </div>
        <div className="bg-circle-1 bg-circle"></div>
        <div className="bg-circle-2 bg-circle"></div>
        <div className="bg-circle-3 bg-circle"></div>
        <div className="bg-circle-4 bg-circle"></div>
      </header>

      <section>
        <Container>
          <Row className="align-items-center">
            <Col lg="12" className="order-lg-1">
              <div className="p-5">
                <h2 className="display-4">What is ToLQC?</h2>
                <p>Currently a database/API for keeping track of data coming out of the sequencing pipeline. There is a separate graphical view, available from the link at the top of this page.</p>
              </div>
            </Col>
          </Row>
        </Container>
      </section>
    </div>
  );
}

export default Home;