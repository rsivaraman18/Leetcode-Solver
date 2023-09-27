''' 821. Shortest Distance to a Character '''

def shortdist(s,c):
    check = [ ]
    
    for i in range(0,len(s)):
        if s[i] ==c:
            check.append(i)

    # Check distance
    stdist = [ ]
    for i in range(0,len(s)):
        small = []
        for num in check:
            new = abs(num - i)
            small.append(new)
        
        stdist.append(min(small))
    print(stdist)
        
        
            
        
    
            
        



shortdist("loveleetcode",'e')
shortdist("aaab",'b')

'''
Input: s = "aaab", c = "b"
Output: [3,2,1,0]

**************************************

Input: s = "loveleetcode", c = "e"
Output: [3,2,1,0,1,0,0,1,2,2,1,0]


'''
