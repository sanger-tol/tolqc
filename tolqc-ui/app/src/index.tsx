/*
SPDX-FileCopyrightText: 2022 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import { createRoot } from 'react-dom/client';
import { 
  Home 
} from './pages';
import reportWebVitals from './reportWebVitals';
import { TolApp, TsDataSource, env } from '@tol/tol-ui'
import Logo from './assets/logo.png';
import './scss/styling.scss';

export const TOLQC_DS = new TsDataSource(
  {
    apiPath: env.API_PATH,
    apiDataPath: env.API_DATA_PATH,
  }
);

const root = createRoot(document.getElementById('root')!);
root.render(
  <TolApp
    boards={{dataSource: TOLQC_DS}}
    brand={
      <img
        src={Logo}
        alt="ToL Portal Logo"
        style={{height: 30}}
      />
    }
    homePage={<Home />}
    pages={[]}
    login={true}
  />
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
