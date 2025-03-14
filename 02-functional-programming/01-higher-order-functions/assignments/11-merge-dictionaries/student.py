# def merge_dictionaries(d1,d2,merge_function):
#     merged=d1.copy()
#     for key,value in d2.items():
#         if key in merged:
#             merged[key]+=value
#     else:
#         merged[key]=value
#     return merged

# def merge_function(value1,value2):
#     return value1+value2

# order1 = {'banana': 4, 'coke': 12, 'chocolate': 3}
# order2 = {'mustard': 1, 'chocolate': 7}
# combined = merge_dictionaries(order1, order2, merge_function)
# print(combined)



def merge_dictionaries(d1,d2,merge_function):
    merged=dict(d1)
    for key,value in d2.items():
        if key in merged:
            merged[key]=merge_function(merged[key],value)
        else:
            merged[key]=value
    return merged

def dict_sum(value1,value2):
    return value1+value2

def dict_average(value1,value2):
    return (value1+value2)/2

# order1 = {'banana': 4, 'coke': 12, 'chocolate': 3}
# order2 = {'mustard': 1, 'chocolate': 7}
january_exams = {'P1': 9, 'FE': 15}
august_exams = {'P1': 7}
combined = merge_dictionaries(january_exams, august_exams, dict_average)
print(combined)