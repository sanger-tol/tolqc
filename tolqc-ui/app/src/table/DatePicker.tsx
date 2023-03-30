/*
SPDX-FileCopyrightText: 2023 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import React from "react";
import { DateRangePicker } from 'rsuite';


export interface Props {
  column: object,
  onFilter: Function
}

export interface State {
  value: any
}

class DatePicker extends React.Component<Props, State> {
  constructor(props: Props) {
    super(props);
    this.state = {
      value: []
    }
    this.filter = this.filter.bind(this);
  }

  filter = (value: any) => {
    this.setState({ value: value });
    this.props.onFilter(value);
  }
  
  render() {
    return (
      <div className='tol-date-picker filter-search-input-hide'>
        <DateRangePicker
          onChange={ this.filter }
          value={ this.state.value }
          format="dd/MM/yyyy"
          size="md"
          placeholder="Select Date Range"
        />
      </div>
    );
  }
}

export default DatePicker;
