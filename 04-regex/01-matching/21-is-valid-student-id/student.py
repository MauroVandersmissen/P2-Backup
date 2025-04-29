import re

def is_valid_student_id(string):
    return bool(re.fullmatch(r"[rsRS]?\d{7}",string))

string="r0948244"
print(is_valid_student_id(string))
string="R0137467"
print(is_valid_student_id(string))
string="s0714281"
print(is_valid_student_id(string))
string="e1234567"
print(is_valid_student_id(string))
string="r1234567890"
print(is_valid_student_id(string))