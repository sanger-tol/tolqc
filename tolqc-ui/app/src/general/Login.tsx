/*
SPDX-FileCopyrightText: 2022 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import { useCallback, useEffect } from 'react';
import { Redirect } from 'react-router-dom';
import { useAuth } from '../contexts/auth.context';
import { getUrlLogin } from '../services/auth/authService';
import { getTokenFromLocalStorage, tokenHasExpired } from '../services/localStorage/localStorageService';
import { LoginIcon } from './Icons';
import '../../../src/scss/_login.scss';


interface LoginProps {
  environment: string;
}

const getLoginClass = (environment: string): string => {
  switch (environment) {
    case "production" || "":
      return "login-light"
  }
  return "login-dark";
}

function Login(props: LoginProps) {
  const { token, setToken } = useAuth();
  useEffect(()=> {
    if(!getTokenFromLocalStorage()){
      setToken('');
    }
    // eslint-disable-next-line
  }, []);

  const login = useCallback(() => {
    getUrlLogin().then((data: any) => {
      window.location.href = data.data.loginUrl;
    });
  }, []);

  return (!token || tokenHasExpired(token)) ? (
    LoginIcon(login, getLoginClass(props.environment))
  ) : (
    <Redirect to="/" />
  );
}

export default Login;