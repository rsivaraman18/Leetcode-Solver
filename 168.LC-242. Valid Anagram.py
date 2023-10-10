''' 242. Valid Anagram '''
def anagram(s,t):
    s1 = ''.join(sorted(s))
    t1 = ''.join(sorted(t))
    if s1 == t1:
        print('Yes anagram')
    else:
        print('Not anangram')
    



anagram("anagram","nagaram")
anagram(s = "rat", t = "car")