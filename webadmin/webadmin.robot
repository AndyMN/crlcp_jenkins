*** Settings ***
Library  Selenium2Library


*** Test Cases ***
FIRST TEST
    OPEN BROWSER    https://www.google.be/      phantomjs
    TITLE SHOULD BE  Google
    CLOSE BROWSER
