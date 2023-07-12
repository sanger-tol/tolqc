# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

*** Settings ***
# config
Variables         ../config_dev.yaml

# Libraries
# Library           SeleniumLibrary
Library           String
Library           OperatingSystem
Library           Collections
Library           Process
Library           DateTime

# Python Sources
# Library            ./pythonlibs/http_utils.py
# Library            ./pythonlibs/database/main.py
# Library            ./pythonlibs/excel_dms_asg.py
# Library            ./pythonlibs/database/DatabaseLibrary/assertion.py
# Library            ./pythonlibs/database/DatabaseLibrary/connection_manager.py
# Library            ./pythonlibs/database/DatabaseLibrary/query.py
# Library            ./pythonlibs/database/DatabaseLibrary/


# Elements
Resource          ./elements/HomePage.robot

# Variables
Resource          ./variables/HomePage.robot

# Keywords
Resource          ./keywords/common/CommonUtils.robot

# Shared
Resource       ../shared/resources/HomePage.resource