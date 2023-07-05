*** Settings ***
Resource          ../../imports.robot
Documentation     Access homepage for all the portals
Library           RPA.Browser.Selenium
Library           RPA.Excel.Files
Library           RPA.HTTP

*** Keywords ***
Access home page of any portal
    Open Available Browser    ${url}