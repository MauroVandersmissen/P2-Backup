def indices_of(xs,condition):
    indices=[]
    for index,string in enumerate(xs):
        if condition(string):
            indices.append(index)
    return indices

def is_palindrom(x):
    return x==x[::-1]

print(indices_of(["kayak", "never", "rotator", "palindrome"],is_palindrom))