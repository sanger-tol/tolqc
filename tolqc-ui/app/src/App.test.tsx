/*
SPDX-FileCopyrightText: 2022 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders home page link', () => {
  render(<App />);
  expect(screen.queryAllByText("Search")).not.toHaveLength(0);
});
