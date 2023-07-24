*** Settings ***
Documentation    Test Suite for login and authentication

Resource       ../resources/vars/common_vars.robot
Library        ../resources/libs/ApiUser.py    ${URL}    ${username}    ${password}

Test Tags      api    login    auth


*** Test Cases ***
Test Authentication And Login
    [Documentation]    Verify authentication and login
    Fetch Token    ${AUTH_URL}
    Login User    ${AUTH_URL}
