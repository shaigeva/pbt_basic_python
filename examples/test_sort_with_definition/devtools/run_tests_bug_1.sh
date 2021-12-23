#!/usr/bin/env bash
set -e
set -x

pipenv run pytest tests/test_sort_bug_1.py
