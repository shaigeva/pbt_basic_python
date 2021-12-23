from hypothesis import given
import hypothesis.strategies as some

from src.reverse_impl import *

@given(some.lists(some.integers()), some.lists(some.integers()))
def test_reverse_correct(lst1, lst2):
    assert reverse_correct(lst2) + reverse_correct(lst1) == reverse_correct(lst1 + lst2)

@given(some.lists(some.integers()), some.lists(some.integers()))
def test_reverse_correct_bug_1(lst1, lst2):
    assert reverse_bug_1(lst2) + reverse_bug_1(lst1) == reverse_bug_1(lst1 + lst2)

@given(some.lists(some.integers()), some.lists(some.integers()))
def test_reverse_correct_bug_2(lst1, lst2):
    assert reverse_bug_2(lst2) + reverse_bug_2(lst1) == reverse_bug_2(lst1 + lst2)

@given(some.lists(some.integers()), some.lists(some.integers()))
def test_reverse_correct_bug_3(lst1, lst2):
    assert reverse_bug_3(lst2) + reverse_bug_3(lst1) == reverse_bug_3(lst1 + lst2)
