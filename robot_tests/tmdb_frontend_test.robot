*** Settings ***
Library          frontend/pages/MainPage.py     Chrome
Suite Setup      Open
Suite Teardown   Close all

*** Test Cases ***
Search Movie
