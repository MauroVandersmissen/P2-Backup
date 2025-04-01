from mystatistics import average
import pytest
from pytest import approx

@pytest.mark.parametrize("ns,expected",[
    ([0.1,0.1,0.1],0.1),
    ([0.5,0.5,0.5],0.5),
    ([0.1,0.2,0.3],0.2),
    ([0.8765,0.09871,0.134567],0.36)])
def test_average(ns,expected):
    actual=average(ns)
    assert approx(expected,abs=0.01)==actual,f"The average of {ns} isn't {expected}"

@pytest.mark.parametrize("ns,expected",[
    ([0.1,0.1,0.1],0.2),
    ([0.10,0.12,0.1],0.12),
    ([0.1987,0.1456,0.09871],0.5)])
def test_not_average(ns,expected):
    actual=average(ns)
    assert not approx(expected,abs=0.01)==actual,f"The average of {ns} is {expected}"