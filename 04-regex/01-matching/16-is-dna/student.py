import re

def is_dna(string):
    return bool(re.fullmatch(r"([GATC])*",string))

string="GA"
print(is_dna(string))
string="gatc"
print(is_dna(string))
string="GATC"
print(is_dna(string))
string="GATCGCTAGCGCTAGATCGATATAGATCGTCGCTAGC"
print(is_dna(string))