/*
SPDX-FileCopyrightText: 2022 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import ReactDOM from 'react-dom';
import { Home } from './pages';
import reportWebVitals from './reportWebVitals';
import { TolApp } from '@tol/tol-ui'
import './scss/styling.scss';


ReactDOM.render(
  <TolApp
    brand='TolQC'
    homePage={<Home />}
    pages={[]}
  />,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
