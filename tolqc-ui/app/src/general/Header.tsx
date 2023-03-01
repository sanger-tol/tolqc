/*
SPDX-FileCopyrightText: 2022 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import React from "react";
import { Container } from "react-bootstrap";
import HeaderButton from "../models/HeaderButton";


export interface Props {
  title: String,
  sub_title?: String,
  buttons?: HeaderButton[]
}

class Header extends React.Component<Props> {
  buttons: HeaderButton[] = [];

  constructor(props: Props) {
    super(props);
    
    if (props.buttons !== undefined) {
      this.buttons = props.buttons
    }
  }

  render() {
    return (
      <div className="header">
        <header className="masthead text-center text-white">
          <div className="masthead-content">
            <Container>
              <div className='navbar-filler'/>
              <h1 className="masthead-heading mb-0">{this.props.title}</h1>
              <h2 className="masthead-subheading mb-0">{this.props.sub_title}</h2>
              {this.buttons.map(button => (
                <a href={button.href} className="btn btn-primary btn-xl rounded-pill mt-5" key={button.text}>{button.text}</a>
              ))}
            </Container>
          </div>
          <div className="bg-circle-1 bg-circle"></div>
          <div className="bg-circle-2 bg-circle"></div>
          <div className="bg-circle-3 bg-circle"></div>
          <div className="bg-circle-4 bg-circle"></div>
        </header>
      </div>
    );
  }
}

export default Header;