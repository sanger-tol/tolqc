// SPDX-FileCopyrightText: 2021 Genome Research Ltd.
//
// SPDX-License-Identifier: MIT

import { createContext, useContext } from 'react';
import { User } from '../models/User'

interface AuthContextValue {
  token: string;
  setToken: (token: string) => void;
  user: User | null;
  setUser: (user: User | null) => void;
}

export const AuthContext = createContext<AuthContextValue>({
  token: '',
  setToken() {
    throw new Error('Missing AuthContext Provider');
  },
  user: null,
  setUser() {
    throw new Error('Missing AuthContext Provider');
  },
});

export const AuthProvider = AuthContext.Provider;
export const useAuth = () => useContext(AuthContext);
