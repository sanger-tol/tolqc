/*
SPDX-FileCopyrightText: 2022 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import { Container } from "react-bootstrap"


function Footer() {
  return (
    <div className="footer">
      <footer className="py-2 bg-black fixed-bottom">
        <Container>
          <p className="m-0 text-center text-white small">Maintained by
            <a href="https://sanger.ac.uk"> Wellcome Sanger Institute</a>
            , <a href="https://www.sanger.ac.uk/programme/tree-of-life/">Tree of Life Programme</a>
            , <a href="https://www.sanger.ac.uk/group/tree-of-life-enabling-platforms/">Enabling Platforms Team</a>
          </p>
        </Container>
      </footer>
    </div>
  );
}

export default Footer;