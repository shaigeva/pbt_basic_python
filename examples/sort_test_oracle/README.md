# Test using a "test oracle"
Test a sorting function using a "test oracle" - an alternative implementation
that serves as resurt-comparison reference.

## The used properties
The test verifies that for every input, the result of the our sort function
is the same as the result of python's built-in sort function.

## Multiple implementations
There are  implementations of the sort algorithm:
- `src/sort_bug.py`
- `src/sort_correct.py`

## Multpile test implementantions
To make the individual test files as simple as possible, I have duplicated the
test code, and the 2 test files (in the `tests` directory) are the same except for the import that get the sort function.</br>

## How to run
In order to run the tests, run one of the test scripts in the `tests` directory:
- `./devtools/run_tests_bug.sh`
- `./devtools/run_tests_correct.sh`

## How the test failures look
### Correct version
`./devtools/run_tests_correct.sh`

As you can expect, there's no failure here. The output looks like this:

```
sort_test_oracle $ ./devtools/run_tests_correct.sh
+ pipenv run pytest tests/test_sort_correct.py
================================== test session starts ===================================
platform darwin -- Python 3.9.6, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /Users/shai/proj/pbt_basic_python/examples/sort_test_oracle
plugins: xdist-2.5.0, forked-1.4.0, hypothesis-6.31.6
collected 1 item

tests/test_sort_correct.py .                                                       [100%]

=================================== 1 passed in 0.55s ====================================
```

### Bug 1
`./devtools/run_tests_bug.sh`

The important part of the failure looks like this
```
>       assert cool_sort(lst) == sorted(lst)
E       assert [0, 0, 1, 0] == [0, 0, 0, 1]
E         At index 2 diff: 1 != 0
E         Use -v to get the full diff

tests/test_sort_bug.py:9: AssertionError
--------------------------------------- Hypothesis ---------------------------------------
Falsifying example: test_sort_is_equivalent_to_test_oracle(
    lst=[1, 0, 0, 0],
)
```
