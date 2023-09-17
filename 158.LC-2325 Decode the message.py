''' 2325. Decode the Message '''


def decode(key,message):
    key = list(key)
    print(key)
    noduplicate = []
    for i in key:
        if i not in noduplicate:
            noduplicate.append(i)
    print(noduplicate)
    





key = "the quick brown fox jumps over the lazy dog",
message = "vkbs bs t suepuv"
decode(key,message)
