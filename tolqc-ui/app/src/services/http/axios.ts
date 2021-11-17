// SPDX-FileCopyrightText: 2021 Genome Research Ltd.
//
// SPDX-License-Identifier: MIT

import axios, { AxiosInstance } from 'axios';

export function createAxiosInstance(options: any): AxiosInstance {
  const axiosInstance = axios.create(
    options
  );

  axiosInstance.interceptors.response.use(
    (response) => {
      return response;
    },
    (error) => {
      throw error; // TODO: handle error like token expired, ...
    }
  );
  return axiosInstance;
}

