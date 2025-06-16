import re

def remove_repeated_words(string):
    # Repeated words pattern (case-insensitive)
    pattern = r'\b(\w+)\b(\s+\1\b)+'
    
    # Replace repeated words with a single occurrence
    return re.sub(pattern, r'\1', string, flags=re.IGNORECASE)

# ChatGPT