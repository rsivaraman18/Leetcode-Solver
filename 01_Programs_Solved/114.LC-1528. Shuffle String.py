'''
Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
'''

def shuffle(s,indices):
    slen = len(s)
    d = { }
    
    for i in range(0,slen):
        d[indices[i]] = s[i]
    print(d)

    fword = ''
    for i in range(0,slen):
        fword = fword + d[i]
    print(fword)
    
        
    




shuffle( "codeleet",[4,5,6,7,0,2,1,3])
shuffle( "abc",[0,1,2])
    
