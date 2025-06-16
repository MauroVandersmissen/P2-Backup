import re

def remove_trailing_whitespace(string):
    # pattern explanation:
    # \s+  --> one or more whitespace characters
    # $    --> end of line
    # re.MULTILINE --> makes $ match the end of each line, not just the whole string
    pattern = r'\s+$'
    
    return re.sub(pattern, '', string, flags=re.MULTILINE)

# ChatGPT