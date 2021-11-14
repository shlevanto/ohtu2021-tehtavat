*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page
Test Teardown  Reset Application

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials  Register
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka 
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials  Register
    Registration Should Fail  Username too short

Register With Valid Username And Too Short Password
    Set Username  kalle
    Set Password  kalle12
    Set Password Confirmation  kalle12
    Submit Credentials  Register
    Registration Should Fail  Password too short

Register With Nonmatching Password And Password Confirmation
    Set Username  kulle
    Set Password  kalle123
    Set Password Confirmation  palle123
    Submit Credentials  Register
    Registration Should Fail  Password and confirmation do not match

Login After Successful Registration
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials  Register
    Registration Should Succeed
    Go To Login Page
    Login Page Should Be Open
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials  Login
    Login Should Succeed

*** Keywords ***
Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail
  [Arguments]  ${message}
  Register Page Should Be Open
  Page Should Contain  ${message}

Set Password Confirmation
    [Arguments]  ${password}
    Input Text  password_confirmation  ${password}
