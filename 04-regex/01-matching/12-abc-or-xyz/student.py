import re

def abc_or_xyz(string):
    return bool(re.fullmatch("(abc)|(xyz)",string))

string="abc"
print(abc_or_xyz(string))
string="xyz"
print(abc_or_xyz(string))
string="chickenpotato"
print(abc_or_xyz(string))