import pytest
from search import Student, linear_search, binary_search

@pytest.mark.parametrize("students", [
    [Student(id) for id in range(0, 100)],
    [],
    [Student(id) for id in [5, 6, 7, 8, 21, 76, 80, 89]]
])
@pytest.mark.parametrize("target_id", range(0, 100))
def test_search(students, target_id):
    expected = linear_search(students, target_id)
    actual = binary_search(students, target_id)
    assert expected == actual