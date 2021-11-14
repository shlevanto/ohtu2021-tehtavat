*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka 
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Registration Should Fail  Username too short

Register With Valid Username And Too Short Password
    Set Username  kalle
    Set Password  kalle12
    Set Password Confirmation  kalle12
    Submit Credentials
    Registration Should Fail  Password too short

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  palle123
    Submit Credentials
    Registration Should Fail  Password and confifmation do not match

*** Keywords ***
Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail
  [Arguments]  ${message}
  Register Page Should Be Open
  Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Text  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Text  password_confirmation  ${password}

Submit Credentials
    Click Button  Register