# Advent of code 2020
*python edition*

## Requirements
* python3
* pip3

## Getting started
* `python3 -m venv .env`
* `source .env/bin/activate`
* `pip3 install -r requirements.txt`

## Virtual environment
To activate: `python3 -m venv .env`
To deactivate: `deactivate`

## Development
### Running tests
Tests can be run using [`pytest`](https://docs.pytest.org/en/stable/).

#### Running all tests
`pytest`
Note: A few days aren't optimized, and some tests are pretty slow.

#### Running all tests for a day
`pytest <DIRECTORY>`
(e.g. `pytest day_04`)

#### Running an individual test
`pytest <PATH_TO_FILE>::<TEST_CLASS_NAME>::<TEST_NAME>`
(e.g. `pytest day_04/test_b.py::TestDay04B::test_valid`)

### Running a problem
`python -m <PATH_TO_SOLUTION>`
(e.g. `python -m day_05.day_05_b.py`)

### Linting
I'm using [flake8](https://flake8.pycqa.org/en/latest/) for linting. To run it:
`flake8`

### Auto-formatting
I'm using [black](https://pypi.org/project/black/) for for auto formatting. To run it:
`black .` (Note the `.` - you need to specify the directory)
