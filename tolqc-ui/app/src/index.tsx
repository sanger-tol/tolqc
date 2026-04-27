/*
SPDX-FileCopyrightText: 2022 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import { createRoot } from "react-dom/client";
import { Home } from "./pages";
import reportWebVitals from "./reportWebVitals";
import { SmartApp, TPageElements, TsDataSource, TOL_DS, env} from "@tol/tol-ui";
import Logo from "./assets/logo.png";
import "./scss/styling.scss";


export const TOLQC_DS = new TsDataSource({
  apiPath: env.API_PATH ,
  apiDataPath: env.API_DATA_PATH
});

export const PAGE_ELEMENTS: TPageElements = {
  home: <Home />,
};

const root = createRoot(document.getElementById("root")!);
root.render(
  <SmartApp
    id="tolqc"
    boards={{ boardDataSource: TOL_DS }}
    brand={<img src={Logo} alt="ToLQC Logo" style={{ height: 30 }} />}
    actionsDataSource={TOLQC_DS}
    pageElements={PAGE_ELEMENTS}
    login={true}
  />,
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
