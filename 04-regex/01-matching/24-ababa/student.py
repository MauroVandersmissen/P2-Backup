import re

def ababa(string):
    return bool(re.fullmatch(r"(.+)(.+)\1\2\1",string))

string="ababa"
print(ababa(string))
string="12121"
print(ababa(string))
string="aba"
print(ababa(string))