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
  timeout: any
}

const onClick = (e: { stopPropagation: () => any; }) => e.stopPropagation();

class TextInput extends React.Component<Props, State> {
  constructor(props: Props) {
    super(props);
    this.state = {
      value: '',
      timeout: null
    }
    this.filter = this.filter.bind(this);
  }

  filter = (value: string) => {
    clearTimeout(this.state.timeout)
    this.setState({
      value: value,
      timeout: setTimeout(() => {
        this.props.onFilter(value);
      }, 800)
    });
  }
  
  render() {
    return (
      <span onClick={ onClick } className='tol-filter-input filter-search-input-hide' id="tol-filter-input">
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
      </span>
    );
  }
}

export default TextInput;
