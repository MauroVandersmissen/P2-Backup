import re

def is_valid_time(string):
    return bool(re.fullmatch(r"\d{2}\:\d{2}\:\d{2}(\.\d{3}){0,3}",string))

string="09:41:45"
print(is_valid_time(string))
string="09:42:54.647"
print(is_valid_time(string))
string="1:2:3.4"
print(is_valid_time(string))