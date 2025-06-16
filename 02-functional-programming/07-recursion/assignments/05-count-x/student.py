# def countX(text):
#     count=0
#     if text.lower=="x":
#         count+=1
#         return count
#     return countX(text[:1])

# print(countX("Xilophone"))

def countX(text):
    if len(text) == 0:
        return 0
    if text[0] == "x":
        return 1 + countX(text[1:])
    else:
        return 0 + countX(text[1:])
    
print(countX("Xilopnone"))
print(countX("Xxx"))
print(countX("Exxon"))