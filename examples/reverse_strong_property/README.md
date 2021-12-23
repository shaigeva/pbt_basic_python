# Test 'reverse' using a strong property
Test implementations of "reverse" list function.

The main reason that this example exists is that `reverse` is a very common
property-based testing example, and is used to illustrate the "round-trip"
pattern.</br>
This is great (and it is one of the examples in this repo), but round-trip
misses a lot of bugs here, including very make-sense bugs.

So I created this example to show how property-based tests can be used to
strongly test `reverse`.

The property that we test is explained as follows:
1. Every list can be thought of as a contcatenation of two sub-lists.
2. If you reverse each of the sublists and then concatenate them **in reverse
   order**, you should get the same thing as if you reversed the original list.

In other words:

```python
assert reverse(lst2) + reverse(lst1) == reverse(lst1 + lst2)
```

## Ideas to note from this example
### Construct the input from parts, instead of generating the entire thing
We COULD generated one list plus an index for slicing the list, but it's much
simpler to just generate two lists, and it's equivalent.

### Try to find a property that "captures what the code does" in some way
It's a little hand-wavy, but concatenating parts in reverse order, feels 
very much related to the essential idea of `reverse`-ing.

## Multiple implementations
The source file contains one correct implementation and 3 incorrect implementations.

## Multpile test implementantions
The test file has multiple tests, all of them test the same property - each one
on a different implementation.

## All the bad implementations are "caught"
Unlike the round-trip example (see `test_reverse_round_trip` in this repo),
in this example all incorrect implementations indeed fail the tests.

Only the correct implentation passes.

## How to run
In order to run the tests, run one of the test scripts in the `tests` directory:
`./devtools/run_tests.sh`

## How the test failures look
Expect to see something like this:

```
reverse_strong_property $ ./devtools/run_tests.sh
+ pipenv run pytest tests/test_reverse_round_trip.py
================================== test session starts ===================================
platform darwin -- Python 3.9.6, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: ~/proj/pbt_basic_python/examples/reverse_strong_property
plugins: xdist-2.5.0, forked-1.4.0, hypothesis-6.31.6
collected 4 items

tests/test_reverse_round_trip.py .FFF                                              [100%]

======================================== FAILURES ========================================
_______________________________ test_reverse_correct_bug_1 _______________________________

    @given(some.lists(some.integers()), some.lists(some.integers()))
>   def test_reverse_correct_bug_1(lst1, lst2):

tests/test_reverse_round_trip.py:11:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

lst1 = [0], lst2 = [1]

    @given(some.lists(some.integers()), some.lists(some.integers()))
    def test_reverse_correct_bug_1(lst1, lst2):
>       assert reverse_bug_1(lst2) + reverse_bug_1(lst1) == reverse_bug_1(lst1 + lst2)
E       assert [1, 0] == [0, 1]
E         At index 0 diff: 1 != 0
E         Use -v to get the full diff

tests/test_reverse_round_trip.py:12: AssertionError
--------------------------------------- Hypothesis ---------------------------------------
Falsifying example: test_reverse_correct_bug_1(
    lst1=[0], lst2=[1],
)
_______________________________ test_reverse_correct_bug_2 _______________________________

    @given(some.lists(some.integers()), some.lists(some.integers()))
>   def test_reverse_correct_bug_2(lst1, lst2):

tests/test_reverse_round_trip.py:15:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

lst1 = [0], lst2 = [1]

    @given(some.lists(some.integers()), some.lists(some.integers()))
    def test_reverse_correct_bug_2(lst1, lst2):
>       assert reverse_bug_2(lst2) + reverse_bug_2(lst1) == reverse_bug_2(lst1 + lst2)
E       assert [1, 0] == [0, 1]
E         At index 0 diff: 1 != 0
E         Use -v to get the full diff

tests/test_reverse_round_trip.py:16: AssertionError
--------------------------------------- Hypothesis ---------------------------------------
Falsifying example: test_reverse_correct_bug_2(
    lst1=[0], lst2=[1],
)
_______________________________ test_reverse_correct_bug_3 _______________________________

    @given(some.lists(some.integers()), some.lists(some.integers()))
>   def test_reverse_correct_bug_3(lst1, lst2):

tests/test_reverse_round_trip.py:19:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

lst1 = [1], lst2 = [0, 0]

    @given(some.lists(some.integers()), some.lists(some.integers()))
    def test_reverse_correct_bug_3(lst1, lst2):
>       assert reverse_bug_3(lst2) + reverse_bug_3(lst1) == reverse_bug_3(lst1 + lst2)
E       assert [0, 0, 1] == [0, 1, 0]
E         At index 1 diff: 0 != 1
E         Use -v to get the full diff

tests/test_reverse_round_trip.py:20: AssertionError
--------------------------------------- Hypothesis ---------------------------------------
Falsifying example: test_reverse_correct_bug_3(
    lst1=[1], lst2=[0, 0],
)
================================ short test summary info =================================
FAILED tests/test_reverse_round_trip.py::test_reverse_correct_bug_1 - assert [1, 0] == ...
FAILED tests/test_reverse_round_trip.py::test_reverse_correct_bug_2 - assert [1, 0] == ...
FAILED tests/test_reverse_round_trip.py::test_reverse_correct_bug_3 - assert [0, 0, 1] ...
============================== 3 failed, 1 passed in 1.01s ===============================
```
