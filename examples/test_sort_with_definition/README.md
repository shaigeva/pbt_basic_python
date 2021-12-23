# Test using propertios that are "the definition of sort"
This test uses simple properties that are essentially the 
"definition of sort" in order to test a sort algorithm.

## The used properties
- A sorted list is ordered from small to large.
- A sorted list contains the same elements as the input list.

## Multiple implementations
There are 3 implementations of the sort algorithm:
- `src/sort_bug_1.py`
- `src/sort_bug_2.py`
- `src/sort_correct.py`

## Multpile test implementantions
To make the individual test files as simple as possible, I have duplicated the
test code, and the 3 test files (in the `tests` directory) are the same except for the import that get the sort function.</br>

### Note - skipped test.
There is **one exception** to this - `tests/test_sort_bug_1.py` has one difference -
one of the tests is marked with "skip". This is done because that test tends to find 
errors that don't shrink well, while the other test does find an easier-to-debug
example.</br>
This is a pretty rare scenario in my experience, but it's worth remembering that if
a shrinked example is still large and clumsy to debug, it might be a good idea to
see if a different property can help us find something that shrinks more nicely.

### Note - large failures
In order to make the examples more interesting, I tried a lot of different bugs,
until I found ones that don't reproduce easily.
Bug_1, for example, is relatively difficult to find - I believe it can't be reproduced
with less than 5 elements in the input list.

## How to run
In order to run the tests, run one of the test scripts in the `tests` directory:
- `./devtools/run_tests_bug_1.sh`
- `./devtools/run_tests_bug_2.sh`
- `./devtools/run_tests_correct.sh`

## How the test failures look
### Correct version
`./devtools/run_tests_correct.sh`

As you can expect, there's no failure here. The output looks like this:

```
test_sort_with_definition $ ./devtools/run_tests_correct.sh
+ pipenv run pytest tests/test_sort_correct.py
==================== test session starts ====================
platform darwin -- Python 3.9.6, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: ~/proj/pbt_basic_python/examples/test_sort_with_definition
plugins: xdist-2.5.0, forked-1.4.0, hypothesis-6.31.6
collected 2 items

tests/test_sort_correct.py ..                         [100%]

===================== 2 passed in 0.82s =====================
```

### Bug 1
`./devtools/run_tests_bug_1.sh`

The important part of the failure looks like this
```
>       assert Counter(cool_sort(lst)) == Counter(lst)
E       assert Counter({-1: 2, 1: 2, 0: 1}) == Counter({-1: 2, 0: 2, 1: 1})
E         Omitting 1 identical items, use -vv to show
E         Differing items:
E         {0: 1} != {0: 2}
E         {1: 2} != {1: 1}
E         Use -v to get the full diff

tests/test_sort_bug_1.py:20: AssertionError
--------------------------------------- Hypothesis ---------------------------------------
Falsifying example: test_sort_contains_the_same_elements(
    lst=[-1, -1, 0, 0, 1],
)
```

### Bug 2
`./devtools/run_tests_bug_2.sh`

The important part of the failure looks like this
```
>           assert sort_res[i] <= sort_res[i+1]
E           assert 1 <= 0

tests/test_sort_bug_2.py:32: AssertionError
--------------------------------------- Hypothesis ---------------------------------------
Falsifying example: test_sort_result_is_ordered(
    lst=[1, 0, 0, 0],
)
```
