def countX(text):
    count=0
    if text.lower=="x":
        count+=1
        return count
    return countX(text[:1])

print(countX("Xilophone"))

# verder uitwerken