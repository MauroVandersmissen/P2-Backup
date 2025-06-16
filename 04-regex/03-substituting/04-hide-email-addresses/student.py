import re

def hide_email_addresses(string):
    # Regex: valid email by given rules, case-insensitive
    pattern = r'\b[a-z0-9.]+@[a-z0-9]+\.[a-z0-9.]*[a-z0-9]+\b'

    # Replace each match with asterisks of the same length
    return re.sub(pattern, lambda m: '*' * len(m.group()), string, flags=re.IGNORECASE)

# ChatGPT