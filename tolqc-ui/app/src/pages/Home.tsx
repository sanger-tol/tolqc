/*
SPDX-FileCopyrightText: 2022 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import React from "react";
import { Header, HeaderButton, CentreContents } from '@tol/tol-ui'

const apiButton: HeaderButton = {
  href: 'api/v1/ui',
  text: 'Use the API'
};

const UIButton: HeaderButton = {
  href: 'api/v1/ui',
  text: 'Use the UI'
};

function Home() {
  return (
    <div className="home">
      <Header
        title="TolQC"
        sub_title="Tree of Life"
        buttons={[apiButton]}
      />
      <CentreContents>
        <h2 className="display-4">What is TolQC?</h2>
        <p>Currently a database/API for keeping track of data coming out of the sequencing pipeline. There is a separate graphical view, available from the link at the top of this page.</p>
      </CentreContents>

    </div>
  );
}

export default Home;