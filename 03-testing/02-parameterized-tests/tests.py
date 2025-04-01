import pytest
from parentheses import matching_parentheses

@pytest.mark.parametrize("string",[("()()()()"),("(())(())"),("((((()))))")])
def testing_matching_parentheses(string):
    assert matching_parentheses(string),f"All parentheses in {string} are matched"

@pytest.mark.parametrize("string",[("())(())"),(")()())(()"),("))))(())")])
def testing_non_matching_parentheses(string):
    assert not matching_parentheses(string),f"Not all parentheses in {string} are matched"