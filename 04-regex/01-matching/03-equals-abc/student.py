import re

string="abc"

def equals_abc(string):
    return bool(re.fullmatch("abc",string))

print(equals_abc(string))