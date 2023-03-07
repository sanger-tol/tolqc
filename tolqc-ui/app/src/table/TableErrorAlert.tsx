/*
SPDX-FileCopyrightText: 2023 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import Alert from "../general/Alert";


const TableErrorAlert = () => (
  <div className="d-flex justify-content-center p-5">
    <Alert 
      type="danger"
      message="See console for errors"
    />
  </div>
)

export default TableErrorAlert;
