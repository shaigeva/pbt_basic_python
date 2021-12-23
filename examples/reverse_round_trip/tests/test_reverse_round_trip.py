from hypothesis import given
import hypothesis.strategies as some

from src.reverse_impl import *

@given(some.lists(some.integers()))
def test_reverse_round_trip_reverse_correct(lst):
    assert reverse_correct(reverse_correct(lst)) == lst

@given(some.lists(some.integers()))
def test_reverse_round_trip_reverse_bug_1(lst):
    assert reverse_bug_1(reverse_bug_1(lst)) == lst

@given(some.lists(some.integers()))
def test_reverse_round_trip_reverse_bug_2(lst):
    assert reverse_bug_2(reverse_bug_2(lst)) == lst

@given(some.lists(some.integers()))
def test_reverse_round_trip_reverse_bug_3(lst):
    assert reverse_bug_3(reverse_bug_3(lst)) == lst
