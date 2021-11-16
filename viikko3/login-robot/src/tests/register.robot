*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command


*** Test Cases ***
Register With Valid Username And Password
  Input Credentials  mikko  mikko123
  Output Should Contain  New user registered


Register With Already Taken Username And Valid Password
  Input Credentials  kalle  kalle1234
  Output Should Contain  User with username kalle already exists


Register With Too Short Username And Valid Password
  Input Credentials  mi  mikko1234
  Output Should Contain  Username must be over 2 characers long


Register With Valid Username And Too Short Password
  Input Credentials  mikko  mik23
  Output Should Contain  Password must be over 7 characers long


Register With Valid Username And Long Enough Password Containing Only Letters
  Input Credentials  mikko  mikkoooooooo
  Output Should Contain  Password cannot contain only letters

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command
