import re

def starts_with_a(string):
    return bool(re.match(r"a",string))

string="abc"
print(starts_with_a(string))
string="potato"
print(starts_with_a(string))
string="a"
print(starts_with_a(string))
string="ahuvkdjdhhjdfhzoiegfbzlkjhf"
print(starts_with_a(string))