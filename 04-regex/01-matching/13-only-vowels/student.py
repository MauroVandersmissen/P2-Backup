import re

def only_vowels(string):
    return bool(re.fullmatch("([aeiou])*",string))

string=""
print(only_vowels(string))
string="abc"
print(only_vowels(string))
string="aeiou"
print(only_vowels(string))
string="a"
print(only_vowels(string))
string="aiiouaaiou"
print(only_vowels(string))