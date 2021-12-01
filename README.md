# advent of code 2016

[![tyler-hoffman](https://circleci.com/gh/tyler-hoffman/aoc-2016.svg?style=svg)](https://circleci.com/gh/tyler-hoffman/aoc-2016)

Python edition

## Getting started
1. `python3 -m venv venv`
1. `source venv/bin/activate`
1. `python3 -m pip install --requirement requirements.txt`

## Commands to run
| Purpose                         | Command |
|---------------------------------|---------|
| Use virtual env                 | `source venv/bin/activate` |
| Deactivate virtual env          | `deactivate` |
| Run all tests                   | `python -m unittest` |
| Run specific test file          | `python -m unittest <FILE>` |
| Run solution file               | `python -m src.day_<DAY>.<PART>` (where `DAY` has a leading zero if needed) |
| Bootstrap files for new problem | `python -m utils.boilerplate.boilerplate -d <DAY> -p <PART>` (where `DAY` has a leading zero if needed) |
| Format code                     | `python -m black .` |

## Handy links
* [AoC](https://adventofcode.com/2016)
* [Repo](https://github.com/tyler-hoffman/aoc-2016)
* [CI](https://app.circleci.com/pipelines/github/tyler-hoffman/aoc-2016)