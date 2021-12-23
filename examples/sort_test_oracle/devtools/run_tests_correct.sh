#!/usr/bin/env bash
set -e
set -x

pipenv run pytest tests/test_sort_correct.py
# Note - this (-n - running tests in parallel) assumes we installed pytest-xdist.
# pipenv run pytest -n 4
