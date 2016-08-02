*** Settings ***
Library  Selenium2Library


*** Test Cases ***
FIRST TEST
    OPEN BROWSER    https://www.google.be/      gc
    TITLE SHOULD BE  Google
    CLOSE BROWSER
