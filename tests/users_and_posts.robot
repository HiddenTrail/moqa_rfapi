*** Settings ***
Documentation    Test Suite for API requests

Resource       ../resources/vars/common_vars.robot
Library        ../resources/libs/ApiUser.py    ${URL}    ${username}    ${password}    ${AUTH_URL}

Test Tags      api    users    posts


*** Test Cases ***
Test Users And Posts Apis
    [Documentation]    Test /users and /posts endpoints
    Get Users
    # TODO: Test GET /posts api
    # TODO: Test GET /users/{user_id}/posts?id={post_id} api
