*** Settings ***
Library          frontend/pages/MainPage.py     Chrome
Library          robot_tests/tmdb_frontend_keywords.py
Suite Setup      Open
Suite Teardown   Close all

*** Test Cases ***
Search Movie
    ${res}      go to discover
    log to console  ${res}
