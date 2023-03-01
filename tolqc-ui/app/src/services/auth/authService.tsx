/*
SPDX-FileCopyrightText: 2022 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import { END_POINT } from '../http/config';
import { httpClient } from '../http/httpClient';


export function getUrlLogin() {
  return httpClient().get(END_POINT.authUrlLogin);
}

export function getToken(dataPost: any) {
  return httpClient().post(END_POINT.authToken, dataPost);
}

export function getProfile(token: string) {
  return httpClient().post(END_POINT.authProfile, {token});
}
