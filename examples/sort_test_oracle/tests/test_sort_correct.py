from hypothesis import given
import hypothesis.strategies as some

# CHOOSE THE SORT FUNCTION
from src.sort_correct import cool_sort

@given(some.lists(some.integers()))
def test_sort_is_equivalent_to_test_oracle(lst):
    assert cool_sort(lst) == sorted(lst)
