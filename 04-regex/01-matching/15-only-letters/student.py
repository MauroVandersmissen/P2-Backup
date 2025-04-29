import re

def only_letters(string):
    return bool(re.fullmatch(r"([a-zA-Z])*",string))

string="potato"
print(only_letters(string))
string="Chicken"
print(only_letters(string))
string="69"
print(only_letters(string))
string="I got tons of potatoes"
print(only_letters(string))