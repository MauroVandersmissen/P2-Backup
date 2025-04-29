import re

def contains_a(string):
    return bool(re.search(r".*a.*",string))

string="a"
print(contains_a(string))
string="abc"
print(contains_a(string))
string="potato"
print(contains_a(string))
string="chicken"
print(contains_a(string))