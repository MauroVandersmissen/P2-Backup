import re

def is_number(string):
    return bool(re.fullmatch(r"\d+(\.\d+)?",string))

string="1"
print(is_number(string))
string="2."
print(is_number(string))
string="34.56"
print(is_number(string))
string="e"
print(is_number(string))
string="123456.,"
print(is_number(string))
string=","
print(is_number(string))
string=""
print(is_number(string))