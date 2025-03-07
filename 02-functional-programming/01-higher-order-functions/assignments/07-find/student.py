def find(items, condition_function):
    for item in items:
        if condition_function(item):
            return item
    return None

def has_consecutive_characters(item):
    for index in range(len(item) - 1):
        if item[index] == item[index + 1]:
            return True
    return False

def find_string_with_consecutive_characters(items):
    return find(items, has_consecutive_characters)

print(find_string_with_consecutive_characters(["monkey", "banana", "computer", "yellow", "oddish"]))
print(find(["monkey", "banana", "computer", "yellow", "oddish"], has_consecutive_characters))