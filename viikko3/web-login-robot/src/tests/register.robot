*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  mikko
    Set Password  mikko123
    Set Password Confirmation  mikko123
    Submit Credentials
    Register Should Succeed

Register With Taken Username And Valid Password
    Set Username  kalle
    Set Password  mikko124
    Set Password Confirmation  mikko124
    Submit Credentials
    Register Should Fail With Message  Username taken
    Register Page Should Be Open


Register With Too Short Username And Valid Password
    Set Username  mi
    Set Password  mikko124
    Set Password Confirmation  mikko124
    Submit Credentials
    Register Should Fail With Message  Username must be over 2 characers long
    Register Page Should Be Open


Register With Valid Username And Too Short Password
    Set Username  mikkoo
    Set Password  mi12
    Set Password Confirmation  mi12
    Submit Credentials
    Register Should Fail With Message  Password must be over 7 characers long
    Register Page Should Be Open

Register With Nonmatching Password And Password Confirmation
    Set Username  mikkoo
    Set Password  mi12kkooo
    Set Password Confirmation  mii2kkoo
    Submit Credentials
    Register Should Fail With Message  Password confirmation does not match
    Register Page Should Be Open

Login After Successful Registration
    Set Username  mikkooo
    Set Password  mikko123
    Set Password Confirmation  mikko123
    Submit Credentials
    Register Should Succeed
    Logout After Registering
    Set Username  mikkooo
    Set Password For Login  mikko123
    Submit Credentials For Login
    Main Page Should Be Open

Login After Failed Registration
    Set Username  mi
    Set Password  mikko124
    Set Password Confirmation  mikko124
    Submit Credentials
    Register Should Fail With Message  Username must be over 2 characers long
    Register Page Should Be Open
    Click Link  Login
    Set Username  mi
    Set Password For Login  mikko124
    Submit Credentials For Login
    Register Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Credentials For Login
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}
    Input Password  password_confirmation  ${password}

Set Password For Login
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open

Logout After Registering
    Click Link  ohtu
    Click Button  Logout


