import re

def correct_dates(string):
    pattern = r'\b(\d{1,2})/(\d{1,2})/(\d+)\b'  # \d+ matches 1 or more digits for year
    return re.sub(pattern, r'\2/\1/\3', string)

# ChatGPT