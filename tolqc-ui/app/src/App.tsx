/*
SPDX-FileCopyrightText: 2021 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import React, { useState }  from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import { Navigation, Footer, Home } from "./pages";
import { getTokenFromLocalStorage,
  getUserFromLocalStorage, 
  tokenHasExpired} from './services/localStorage/localStorageService';
import { AuthProvider } from './contexts/auth.context';
import { Redirect } from 'react-router-dom';

import 'bootstrap/dist/css/bootstrap.min.css';
import './scss/one-page-wonder.scss';


function App() {
  const [token, setToken] = useState(getTokenFromLocalStorage);
  const [user, setUser] = useState(getUserFromLocalStorage);

    return (
    <div className="App">
      <AuthProvider
        value={{
          token,
          setToken,
          user,
          setUser,
        }}
      >
        <Router>
          <Navigation />
          <Switch>
            <Route path="/" exact component={() => <Home />} />
          </Switch>
          <Footer />
        </Router>
      </AuthProvider>
    </div>
  );
}

export default App;