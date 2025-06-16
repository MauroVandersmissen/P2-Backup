def findMaximum(list):
    if not list:
        raise IndexError("List cannot be empty.")
    if len(list) == 1:
        return list[0]
    rest = findMaximum(list[1:])
    return list[0] if list[0] > rest else rest
    
print(findMaximum([1,2,3,6,4]))

# Beide versies werken hetzelfde

def findMaximum(lst):
    if not lst:
        raise IndexError("List cannot be empty.")
    if len(lst) == 1:
        return lst[0]
    return max(lst[0], findMaximum(lst[1:]))

print(findMaximum([1,2,3,6,4]))