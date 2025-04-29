import re

def contains_three_digits(string):
    return bool(re.fullmatch(r".*\d.*\d.*\d.*",string))

string="1"
print(contains_three_digits(string))
string="548868"
print(contains_three_digits(string))
string="123"
print(contains_three_digits(string))
string="1a2b3c"
print(contains_three_digits(string))