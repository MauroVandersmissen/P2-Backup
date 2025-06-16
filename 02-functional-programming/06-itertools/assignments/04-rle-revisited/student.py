# def rle_encode(data):
#     iterable=iter(data)
#     try:
#         current_char=next(iterable)
#         count=1
#         for char in iterable:
#             if char==current_char:
#                 count+=1
#             else:
#                 yield (current_char,count)
#                 current_char=char
#                 count=1
#         yield (current_char,count)
#     except StopIteration:
#         pass

# def rle_decode(data):
#     for char,count in data:
#         for _ in range(count):
#             yield char

# data="poooootaaaaaatooooooooos"
# encoded=rle_encode(data)
# print("Encoded:",list(encoded))

# encoded=rle_encode(data)
# decoded=rle_decode(encoded)
# print("Decoded:","".join(decoded))

from itertools import groupby, chain

def rle_encode(data):
    for char, group in groupby(data):
        count = sum(1 for _ in group)
        yield (char, count)

def rle_decode(data):
    return chain.from_iterable(char * count for char, count in data)

data = "pooooootaaaaaaaaaaaatooooooooos"
encoded = list(rle_encode(data))
print("Encoded:", encoded)

encoded = rle_encode(data)
decoded = rle_decode(encoded)
print("Decoded:", "".join(decoded))