*** Settings ***
Library           OperatingSystem

*** Keywords ***
Log all variables
    Log To Console    \nEnvironment Variables\n-------------------
    ${env_variables}=    Log Environment Variables
    FOR    ${item}    IN    @{env_variables.items()}
        Log To Console    ${item[0]} = ${item[1]}
    END
    Log To Console    \nVariables\n-------------------
    ${variables}=    Get Variables
    FOR    ${item}    IN    @{variables.items()}
        Log To Console    ${item[0]} = ${item[1]}
    END
