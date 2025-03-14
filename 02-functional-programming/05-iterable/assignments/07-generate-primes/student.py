import math

# def is_prime(n):
#     if n <= 1:
#         return False
#     elif n == 2:
#         return True
#     elif n % 2 == 0:
#         return False
    
#     for i in range(3, int(math.sqrt(n)) + 1, 2):
#         if n % i == 0:
#             return False
#     return True

def is_prime(n):
    if n<2:
        return False
    return not any(n%divider==0 for divider in range(2,n))

def primes():
    yield 2
    number=1
    getal=1
    while True:
        while number>getal and number%getal!=0:
            getal+=1
            if number == getal:
                yield number
        number+=1
        getal=2


# print(is_prime(7))
ps=primes()
print(next(ps))
print(next(ps))
print(next(ps))
print(next(ps))
print(next(ps))