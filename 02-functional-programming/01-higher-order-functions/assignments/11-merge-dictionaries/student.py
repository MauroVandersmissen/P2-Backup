def merge_dictionaries(d1,d2,merge_function):
    merged={}
    if d1.key in d2:
        merge_function(d1.value,d2.value)
    else:
        merged.add(d1,d2)