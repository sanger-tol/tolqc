/*
SPDX-FileCopyrightText: 2023 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import Alert from "../general/Alert";


const TableErrorAlert = () => (
  <div className="d-flex justify-content-center p-5">
    <Alert 
      type="danger"
      message="See console for errors - please ensure you have a working database"
    />
  </div>
)

export default TableErrorAlert;
