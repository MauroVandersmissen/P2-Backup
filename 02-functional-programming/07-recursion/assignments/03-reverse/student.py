# def test(text):
#     for char in text:
#         print(char)

def reverse_from_left(text):
    if len(text)<=1:
        return text
    return reverse_from_left(text[1:])+text[0]

def reverse_from_right(text):
    if len(text)<=1:
        return text
    return text[-1]+reverse_from_right(text[:-1])

print(reverse_from_left("potato"))
print(reverse_from_right("potato"))
# test("abcd")