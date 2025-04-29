import re

def thrice_repeated(string):
    return bool(re.fullmatch(r"(.+)\1\1",string))

string="aa"
print(thrice_repeated(string))
string="11"
print(thrice_repeated(string))
string="a1"
print(thrice_repeated(string))
string="aaa"
print(thrice_repeated(string))
string="111"
print(thrice_repeated(string))
string="a1a"
print(thrice_repeated(string))