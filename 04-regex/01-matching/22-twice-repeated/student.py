import re

def twice_repeated(string):
    return bool(re.fullmatch(r"(.)\1",string))

string="aa"
print(twice_repeated(string))
string="11"
print(twice_repeated(string))
string="a1"
print(twice_repeated(string))
string="aaa"
print(twice_repeated(string))