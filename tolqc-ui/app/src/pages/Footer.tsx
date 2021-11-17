/*
SPDX-FileCopyrightText: 2021 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import React from "react";
import { Container } from "react-bootstrap"


function Footer() {
  return (
    <div className="footer">
      <footer className="py-2 bg-black fixed-bottom">
        <Container>
          <p className="m-0 text-center text-white small">Maintained by
            <a href="https://sanger.ac.uk"> Wellcome Sanger Institute</a>
            , <a href="https://www.sanger.ac.uk/programme/tree-of-life/">Tree of Life programme</a>
            , <a href="mailto:tol-platforms@sanger.ac.uk">Enabling Platforms team</a>
          </p>
        </Container>
      </footer>
    </div>
  );
}

export default Footer;