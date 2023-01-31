/*
SPDX-FileCopyrightText: 2022 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import React from "react";
import { AutoTable, CentreContents } from '@tol/tol-ui'

function Home() {
  return (
    <div className="home">
      <CentreContents>
        <AutoTable endpoint="species"
        />
      </CentreContents>

    </div>
  );
}

export default Home;