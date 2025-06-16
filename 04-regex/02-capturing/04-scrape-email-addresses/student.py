import re

def scrape_email_addresses(string):
    # Regex pattern to match valid email addresses according to the rules:
    # - Before the @: one or more lowercase letters, digits, or dots [a-z0-9.]+
    # - Exactly one '@' symbol
    # - After the @: one or more lowercase letters or digits [a-z0-9]+
    # - At least one dot '.' followed by one or more lowercase letters or digits (repeated one or more times)
    #   This is grouped as a non-capturing group (?:\.[a-z0-9]+)+ to avoid capturing only part of the domain
    # - \b ensures word boundaries so we don't match inside larger strings
    pattern = r'\b[a-z0-9.]+@[a-z0-9]+(?:\.[a-z0-9]+)+\b'

    # Use re.findall to return all matches in the input string
    # flags=re.IGNORECASE makes the regex case-insensitive (so uppercase letters are allowed)
    return re.findall(pattern, string, flags=re.IGNORECASE)

#ChatGPT