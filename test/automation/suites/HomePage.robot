# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

*** Settings ***
Resource       ../resources/imports.robot
# Library        RPA.Browser.Selenium
# Library        RPA.Excel.Files
# Library        RPA.FileSystem
# Library        RPA.HTTP
# Library        RPA.PDF

*** Test Cases ***
TC_1_1 - User should be able to browser home page of the portal
    [Documentation]   User should be able to browser home page of the portal
    Access home page of any portal
    Wait Until Page Contains    Maintained by Wellcome Sanger Institute, Tree of Life Programme, Enabling Platforms Team