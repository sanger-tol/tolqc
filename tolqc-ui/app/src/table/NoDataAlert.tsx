/*
SPDX-FileCopyrightText: 2022 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import Alert from "../general/Alert";


const NoDataAlert = () => (
  <div className="d-flex justify-content-center p-5">
    <Alert 
      type="warning"
      message="No data found"
    />
  </div>
)

export default NoDataAlert;
