/*
SPDX-FileCopyrightText: 2022 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import { useEffect, useState } from 'react';
import { useHistory } from 'react-router-dom';
import { useAuth } from '../contexts/auth.context';
import {getProfile, getToken} from '../services/auth/authService';
import { useQuery } from '../hooks/useQuery';
import { setTokenToLocalStorage, setUserToLocalStorage, tokenHasExpired } from '../services/localStorage/localStorageService';

export function Callback() {
  const history = useHistory();
  const { setToken, token, setUser } = useAuth();
  const [state] = useState(useQuery().get('state') || undefined);
  const [tokenCode] = useState(useQuery().get('code') || undefined);

  useEffect(() => {
    if (!token || tokenHasExpired(token)) {
      const stateToken = {
        state,
        code: tokenCode,
      };
      getToken(stateToken)
        .then((res: any) => {
          const data = res.data;
          setTokenToLocalStorage(data.access_token);
          setToken(data.access_token);
          getProfile(data.access_token)
          .then((data2: any) => {
            setUserToLocalStorage(data2.data);
            setUser(data2.data);
          })
          .finally(() => {
            let targetUrl = localStorage.getItem('returnUrl') || '';
            if (!targetUrl || targetUrl === 'index') {
              targetUrl = '/';
            }
            history.replace(targetUrl);
          });
        })
        .catch(() => { 
          history.replace('/login');
        });
    }
    // eslint-disable-next-line
  }, []);

  return null;
}

export default Callback