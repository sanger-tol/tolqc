/*
SPDX-FileCopyrightText: 2023 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import React from 'react';
import ToolTipOverlay from '../general/TooltipOverlay';


export interface Props {
  text: string, 
  contents: string
}

class CellTooltip extends React.Component<Props> {
  render() {
    const { text, contents } = this.props;
    return (
      <ToolTipOverlay
        contents={ contents }
      >
        <div className='tooltip-wrapper'>
          { text }
        </div>
      </ToolTipOverlay>
    );
  }
}

export default CellTooltip;
