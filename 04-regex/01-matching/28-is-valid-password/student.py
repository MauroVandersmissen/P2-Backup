# import re

# def is_valid_password(string):
#     return bool(re.match(r"[a-zA-Z0-9+-*/.@]{12,}",string))

# string="abc"
# print(is_valid_password(string))
# string="123456789101112"
# print(is_valid_password(string))
# string="Potato12345*"
# print(is_valid_password(string))

import re
from collections import Counter

def is_valid_password(string):
    pattern = (
        r'^(?!.*(.)\1\1)'
        r'(?=.*[a-z])'
        r'(?=.*[A-Z])'
        r'(?=.*\d)'
        r'(?=.*[+\-*/.@])'
        r'[a-zA-Z0-9+\-*/.@]{12,}$'
    )

    if not re.match(pattern, string):
        return False

    counts = Counter(string)
    if any(count >= 4 for count in counts.values()):
        return False

    return True

string="Abc123+@Defg"
print(is_valid_password(string)) #true
string="aaaBBB111+@aaa"
print(is_valid_password(string)) #false
string="A1b2C3+@abcabc"
print(is_valid_password(string)) #true
string="Valid1+Pass@Wrd"
print(is_valid_password(string)) #true
