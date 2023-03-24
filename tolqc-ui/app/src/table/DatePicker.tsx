/*
SPDX-FileCopyrightText: 2023 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import React from "react";
import { DateRangePicker } from 'rsuite';

const DatePicker = () => {
  const [value, setValue] = React.useState(null);

  console.log(value)

  return (
    <div className='tol-date-picker filter-search-input-hide'>
      <DateRangePicker
        block
        value={value}
        onChange={setValue}
        format="dd/MM/yyyy"
        placeholder="Select Date Range"
      />
    </div>
  );
}

export default DatePicker;
