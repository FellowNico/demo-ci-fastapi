Demonstration of an example CI for fastapi and poetry
-----------------------------------------------------

Event: pull-request

Environment configuration of CI:

- python-version: ["3.8", "3.9"]
- poetry-version: ["1.0", "1.1.15"]
- os: [ubuntu-18.04]

Github Actions CI steps:

- setup-python
- setup-poetry
- install dependencies
- linting with flake8
- test with pytest
