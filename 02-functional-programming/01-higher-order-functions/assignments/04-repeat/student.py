def say_hello():
    print("Hello!")

def repeat(function,number):
    for i in range(number):
        function()

repeat(say_hello,5)