from collections import Counter

# I'm intentionally leaving some unused imports because there's some 
# commented-out code that uses these imports
from hypothesis import given, example, settings, Phase
import hypothesis.strategies as some
from pytest import skip
from pytest import mark

# CHOOSE THE SORT FUNCTION
from src.sort_bug_1 import cool_sort

# Uncomment to skip test
# @mark.skip("")
@given(some.lists(some.integers()))
# @settings(verbosity=Verbosity.verbose)
# Uncomment to disable shrinking (the last phase of the test is shrinking)
# @settings(phases=(Phase.explicit, Phase.reuse, Phase.generate, Phase.target))
def test_sort_contains_the_same_elements(lst):
    assert Counter(cool_sort(lst)) == Counter(lst)

# NOTE: TEST IS SKIPPED because it tends to find failures that don't shrink well.
# (pretty rare scenario).
@mark.skip("")
@given(some.lists(some.integers()))
# Uncomment to disable shrinking (the last phase of the test is shrinking)
# @settings(phases=(Phase.explicit, Phase.reuse, Phase.generate, Phase.target))
# @settings(max_examples=100)
def test_sort_result_is_ordered(lst):
    sort_res = cool_sort(lst)
    for i in range(len(lst) - 1):
        assert sort_res[i] <= sort_res[i+1]
