def fizzbuzz():
    i=0
    while True:
        i+=1
        if i % 3 == 0 and i % 5 == 0:
            yield "fizzbuzz"
        elif i % 3 == 0:
            yield "fizz"
        elif i % 5 == 0:
            yield "buzz"
        else:
            yield str(i)
var=fizzbuzz()
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))