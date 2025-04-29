import re

def only_digits(string):
    return bool(re.fullmatch(r"\d*",string))

string="1"
print(only_digits(string))
string="23456789"
print(only_digits(string))
string="0 potatoes"
print(only_digits(string))