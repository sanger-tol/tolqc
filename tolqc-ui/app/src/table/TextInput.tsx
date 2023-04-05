/*
SPDX-FileCopyrightText: 2023 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import React from "react";
import { Input, InputGroup } from 'rsuite';
import SearchIcon from '@rsuite/icons/Search';
import { stopPropagation } from '../general/Utils'


export interface Props {
  column: object,
  onFilter: Function
  type: string
}

export interface State {
  value: any
  timeout: any
}

class TextInput extends React.Component<Props, State> {
  constructor(props: Props) {
    super(props);
    this.state = {
      value: '',
      timeout: null
    }
    this.filter = this.filter.bind(this);
  }

  validateInput = (value: string) => {
    const { type } = this.props
    const intRegex = /^[-]?[0-9\b]*$|^$/
    const floatRegex = /^[-]?\d*(\.\d*)?$|^$/
    if (type === 'int' && !value.match(intRegex)) {
      return true
    } else if (type === 'float' && !value.match(floatRegex)) {
      return true
    }
  }

  filter = (value: string) => {
    if (this.validateInput(value)) { return }
    // can start with minus or period but won't call endpoint
    if (value === '-' || value === '.') {
      this.setState({
        value: value
      })
    } else {
      clearTimeout(this.state.timeout)
      this.setState({
        value: value,
        timeout: setTimeout(() => {
          this.props.onFilter(value);
        }, 800)
      });
    }
  }
  
  render() {
    return (
      <span onClick={ stopPropagation } className='tol-filter-input filter-search-input-hide' id="tol-filter-input">
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
