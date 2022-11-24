// SPDX-FileCopyrightText: 2022 Genome Research Ltd.
//
// SPDX-License-Identifier: MIT

export const CONFIG = {
  baseURL: '/api/v1',
  headers: {
    'Content-Type': 'application/json',
  },
};

export const END_POINT = {
  authUrlElixir: '/auth/login',
  authToken: '/auth/token',
  authProfile: '/auth/profile',
  authLogout: '/auth/logout',
};
