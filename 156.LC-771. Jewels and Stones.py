'''  771. Jewels and Stones '''

def jewel(jewels,stones):
    jcount = []
    for i in jewels:
        num = stones.count(i)
        jcount.append(num)
    print(jcount)
    jsum = 0
    for num in jcount:
        jsum = jsum + num
    print(jsum)
        


jewel("aA", stones = "aAAbbbb")
jewel("z", stones = "ZZ")
