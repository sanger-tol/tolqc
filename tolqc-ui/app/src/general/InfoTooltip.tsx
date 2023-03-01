/*
SPDX-FileCopyrightText: 2023 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import React from 'react';
import { InfoIcon } from './Icons';
import ToolTipOverlay from './TooltipOverlay';


export interface Props {
  contents: string
}

class InfoTooltip extends React.Component<Props> {
  render() {
    return (
      <ToolTipOverlay
        contents={ this.props.contents }
      >
        <div className='tooltip-wrapper'>
          <InfoIcon />
        </div>
      </ToolTipOverlay>
    );
  }
}

export default InfoTooltip;
