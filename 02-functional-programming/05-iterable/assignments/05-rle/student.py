def rle_encode(data):
    iterable=iter(data)
    try:
        current_char=next(iterable)
        count=1
        for char in iterable:
            if char==current_char:
                count+=1
            else:
                yield (current_char,count)
                current_char=char
                count=1
        yield (current_char,count)
    except StopIteration:
        pass

def rle_decode(data):
    for char,count in data:
        for _ in range(count):
            yield char

data="poooootaaaaaatooooooooos"
encoded=rle_encode(data)
print("Encoded:",list(encoded))

encoded=rle_encode(data)
decoded=rle_decode(encoded)
print("Decoded:","".join(decoded))