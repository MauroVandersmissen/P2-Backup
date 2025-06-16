import pytest
from pytest import approx
from mergesort import split_in_two, merge_sorted, merge_sort
from itertools import permutations

@pytest.mark.parametrize("ns", [
    list(range(n)) for n in range(100)
])
def test_split_in_two(ns):
    actual = ns
    left, right = split_in_two(ns)

    assert len(left) == approx(len(right), 1)
    assert actual == left + right

@pytest.mark.parametrize("left", [
    [],
    [1],
    [1, 2, 3],
    [9, 18, 97, 157],
    [5, 5, 6, 2, 4, 4]
])
@pytest.mark.parametrize("right", [
    [],
    [2],
    [4, 5, 6],
    [7, 67, 781, 1764, 45685],
    [44, 0, 0, 77, 36, 44, 77, 77, 23456789]
])
def test_merge_sorted(left, right):
    assert merge_sorted(left, right) == sorted(left + right)

@pytest.mark.parametrize("expected, ns", [
    *[([1, 2, 3], list(p)) for p in permutations([1, 2, 3])],
    *[([], list(p)) for p in permutations([])],
    *[([1, 2, 3, 4, 5, 6], list(p)) for p in permutations([1, 2, 3, 4, 5, 6])],
    *[([1, 1, 2, 2, 3, 3], list(p)) for p in permutations([1, 1, 2, 2, 3, 3])],
    *[([2, 5, 9, 10, 657, 764656], list(p)) for p in permutations([2, 5, 9, 10, 657, 764656])]
])
def test_merge_sort(expected, ns):
    actual = merge_sort(ns)
    assert actual == expected