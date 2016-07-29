*** Settings ***
Variables  auth_vars.py
Library  CrlCpLib.py    ${USERNAME}     ${PASSWORD}
Suite Setup     CHECK CREDENTIALS   ${BASE_URL}         # Checks if we can login to the given url with auth vars. If this fails no test will run

*** Variables ***
${BASE_URL}   https://prometheus.desy.de/Users/${USERNAME}/Private/

${FILE_DIR}     /scratch/jenkins/jenkins/workspace/RobotIntro/
${FILE_NAME}    testfile


*** Test Cases ***
FILE COPY
    COPY FILE TO    ${FILE_DIR}${FILE_NAME}   ${BASE_URL}${FILE_NAME}
    STATUS CODE SHOULD BE   201

FILE DELETE
    DELETE FILE  ${BASE_URL}${FILE_NAME}
    STATUS CODE SHOULD BE  204

FILE DOWNLOAD
    DOWNLOAD FILE AS    ${BASE_URL}notice    ${FILE_DIR}notice
    STATUS CODE SHOULD BE   200

