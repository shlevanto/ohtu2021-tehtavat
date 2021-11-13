*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
  Input Credentials  kalle  kalle123kalle
  Output Should Contain  New user registered

Register With Already Taken Username And Password
  Input Credentials  palle  kalle123kalle
  Output Should Contain  This username is taken

Register With Too Short Username And Valid Password
  Input Credentials  pa  kalle123kalle
  Output Should Contain  Username too short

Register With Valid Username And Too Short Password
  Input Credentials  kalle  ka123
  Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
  Input Credentials  kalle  kallekalle
  Output Should Contain  Password can not be only letters

*** Keywords ***
Input New Command And Create User
  Create User  palle  palle69palle
  Input New Command
  