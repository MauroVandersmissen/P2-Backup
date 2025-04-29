import re

string="a"

def equals_a(string):
    return bool(re.fullmatch("a",string))

print(equals_a(string))