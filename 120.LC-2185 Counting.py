
'''2185. Counting Words With a Given Prefix'''

def countword(words,pref):
    li = []
    plen = len(pref)
    for i in words:
        out = ''
        new = i[0:plen]
        if new == pref:
            li.append(i)
    print(li)
    print(len(li))
        
    




countword(["pay","attention","practice","attend"] , "at")
countword(["leetcode","win","loops","success"],"code")
