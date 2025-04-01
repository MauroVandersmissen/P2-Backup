from intervals import overlapping_intervals


def test_overlapping_intervals():
    assert overlapping_intervals((1, 5), (3, 6))
    assert overlapping_intervals((1,6),(5,9))
    assert overlapping_intervals((1,5),(3,4))
    assert overlapping_intervals((1,5),(1,1))
    assert overlapping_intervals((0,5),(5,10))
    assert overlapping_intervals((1,1),(1,9))
    assert overlapping_intervals((2,3),(1,4))
    assert not overlapping_intervals((2, 5), (7, 10))
    assert not overlapping_intervals((1,4),(5,7))
    assert not overlapping_intervals((0,4),(4,0))
    assert not overlapping_intervals((4,0),(0,4))