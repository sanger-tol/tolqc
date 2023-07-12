# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

*** Settings ***
Resource          ../../resources/imports.robot
Library           RPA.Browser.Selenium
# Library           RPA.Excel.Files
# Library           RPA.HTTP

*** Keywords ***
Access home page of any portal
    Open Available Browser    ${url}