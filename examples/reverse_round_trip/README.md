# Test using a round-trip property
Test implementations of "reverse" list function using round-trip:
```python
assert reverse(reverse(lst)) == lst
```
This test uses simple properties that are essentially the 
"definition of sort" in order to test a sort algorithm.

## Multiple implementations
The source file contains one correct implementation and 3 incorrect implementations.

## Multpile test implementantions
The test file has multiple tests, all of them test the same property - each one
on a different implementation.

## ONLY SOME OF THE TESTS FAIL!
This example serves to illustrate 2 points:
1. Round-trip is easy to use and is a great pattern.
1. Round-trip doesn't catch all bugs.

In this example, 2 of the incorrect implementations actually pass the round-trip
test, because they are incorrect in way that also "satisfies round-trip".

Only one incorrect implementation fails - `reverse_bug_3`.

If you'd like to see how to use property-based testing to test `reverse` more
thoroughly, have a look at the example `reverse_strong_property` (in this repo).


## How to run
In order to run the tests, run one of the test scripts in the `tests` directory:
`./devtools/run_tests.sh`

## How the test failures look
As explained above - only one of the tests fail.</br>
Expect to see something like this:

```
reverse_round_trip $ ./devtools/run_tests.sh
+ pipenv run pytest tests/test_reverse_round_trip.py
================================== test session starts ===================================
platform darwin -- Python 3.9.6, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: ~/proj/pbt_basic_python/examples/reverse_round_trip
plugins: xdist-2.5.0, forked-1.4.0, hypothesis-6.31.6
collected 4 items

tests/test_reverse_round_trip.py ...F                                              [100%]

======================================== FAILURES ========================================
_________________________ test_reverse_round_trip_reverse_bug_3 __________________________

    @given(some.lists(some.integers()))
>   def test_reverse_round_trip_reverse_bug_3(lst):

tests/test_reverse_round_trip.py:19:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

lst = [0, 0, 1]

    @given(some.lists(some.integers()))
    def test_reverse_round_trip_reverse_bug_3(lst):
>       assert reverse_bug_3(reverse_bug_3(lst)) == lst
E       assert [0, 1, 0] == [0, 0, 1]
E         At index 1 diff: 1 != 0
E         Use -v to get the full diff

tests/test_reverse_round_trip.py:20: AssertionError
--------------------------------------- Hypothesis ---------------------------------------
Falsifying example: test_reverse_round_trip_reverse_bug_3(
    lst=[0, 0, 1],
)
================================ short test summary info =================================
FAILED tests/test_reverse_round_trip.py::test_reverse_round_trip_reverse_bug_3 - assert...
============================== 1 failed, 3 passed in 0.94s ===============================

```
