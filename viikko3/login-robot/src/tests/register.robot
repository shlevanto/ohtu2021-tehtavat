*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
  Input Credentials  kalle  kalle123kalle
  Output Should Contain  New user registered

*** Keywords ***
Input New Command And Create User
  Create User  palle  palle69palle
  Input New Command
  