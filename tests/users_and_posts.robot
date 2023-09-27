*** Settings ***
Documentation    Test Suite for API requests

Resource       ../resources/vars/common_vars.robot
Library        ../resources/libs/ApiUser.py    ${URL}    ${username}    ${password}    ${AUTH_URL}

Test Tags      api    users    posts


*** Test Cases ***
Verify Users Api
    [Documentation]    Verify /users endpoint
    Get Users
    # TODO: Verify users response

Verify Posts Api
    [Documentation]    Verify /posts endpoint
    Pass Execution    Testing /posts API
    # TODO: Test GET /posts api

Verify Users Api With Filtering UserId and PostId
    [Documentation]    Verify /users/user_id/posts endpoint with filtering
    Pass Execution    Testing /users/user_id/posts API
    # TODO: Test GET /users/{user_id}/posts?id={post_id} api
