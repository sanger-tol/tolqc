/*
SPDX-FileCopyrightText: 2023 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import React from "react";
import { Input, InputGroup } from 'rsuite';
import SearchIcon from '@rsuite/icons/Search';


export interface Props {
  column: object,
  onFilter: Function
}

export interface State {
  value: any
}

class TextInput extends React.Component<Props, State> {
  constructor(props: Props) {
    super(props);
    this.state = {
      value: ''
    }
    this.filter = this.filter.bind(this);
  }

  filter = (value: string) => {
    this.setState({ value: value });
    this.props.onFilter(value);
  }
  
  render() {
    return (
      <div className='tol-filter-input filter-search-input-hide'>
        <InputGroup inside>
          <Input
            onChange={ this.filter }
            value={ this.state.value }
            placeholder={ this.props.column['text'] }
          />
          <InputGroup.Addon>
            <SearchIcon />
          </InputGroup.Addon>
        </InputGroup>
      </div>
    );
  }
}

export default TextInput;
