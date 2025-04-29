import re

string="b"

def equals_b(string):
    return bool(re.fullmatch("b",string))

print(equals_b(string))