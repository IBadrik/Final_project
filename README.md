# Final_project
This repository contains the final study project automation QA on python
This file contains test-cases https://docs.google.com/spreadsheets/d/1fF5-OJJ2f86ZOdQJ5Pk5fyb1v3m4BgFZx7lGCgwnIRE/edit#gid=0

File "conftest.py" contains fixtures. Just one, but I think that's enough :)

File "test_register_page_RT" contains tests of register page. Several tests use test design techniques: boundary values and equivalence classes. 

File "test_auth_page_RT" contains tests of authorization page.

File "test_password_recovery_page_RT" contains tests of password recovery page.

Run tests: python3 -m pytest -v --driver Chrome --driver-path <chromedriver_directory>/chromedriver test_<file_name>.py
