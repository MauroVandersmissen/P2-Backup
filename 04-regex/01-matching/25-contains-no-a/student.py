import re

def contains_no_a(string):
    return bool(re.fullmatch(r"[^a]*",string))

string="contains_no_a"
print(contains_no_a(string))
string="potato"
print(contains_no_a(string))
string="eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"
print(contains_no_a(string))