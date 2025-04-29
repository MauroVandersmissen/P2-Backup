import re

def is_valid_email_address(string):
    return bool(re.fullmatch(r"[a-z0-9.]+@(ucll\.be|student\.ucll\.be)",string))

string="potato@ucll.be"
print(is_valid_email_address(string))
string="poatochicken.bom"
print(is_valid_email_address(string))
string="potato@chicken"
print(is_valid_email_address(string))
string="barry.protter@student.ucll.be"
print(is_valid_email_address(string))