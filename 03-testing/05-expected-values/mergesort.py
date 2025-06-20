# def split_in_two(ns):
#     middle = int(len(ns) / 2)
#     left = ns[:middle]
#     right = ns[middle:]
#     return left, right

def split_in_two(ns):
    middle = len(ns) // 2
    return ns[:middle], ns[middle:]

def merge_sorted(left, right):
    left = sorted(left)
    right = sorted(right)
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(ns):
    if len(ns) <= 1:
        return ns

    left, right = split_in_two(ns)
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    return merge_sorted(sorted_left, sorted_right)

print(split_in_two([1, 2, 3, 4, 5, 6, 7]))
left, right = split_in_two([1, 2, 3, 4, 5, 6, 7])
print(merge_sorted(left, right))
print(merge_sort([6, 3, 8, 1, 9, 2]))