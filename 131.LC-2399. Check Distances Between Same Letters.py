''' 2399. Check Distances Between Same Letters '''

def distance(s,distance):
    alpha = []
    for i in range(97,123):
        alpha.append(chr(i))
    #print(alpha)
    li = [ ]
    slen = len(s)/2

    for i in range(97,123):
        ch = chr(i)
        
        if ch in s:
            first    = s.find(ch)
            second   = s.find(ch,first+1)
            li.append( (second-first)-1 )
            
        else:
            li.append(0)
            
    # customize distance
    i = 0
    for letter in alpha:
        if letter in s:
            pass
          
        else:
            distance[i] =0
            
        i = i+1   
            
        
        
    #print(distance)
    
    # check two arrays
    if li == distance:
        print('True')
        return True
    else:
        print('False')
        return False
    
    
    

# range(0,26):
       
        
#distance('abaccb',[1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

#distance(s = "aa", distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] )

distance('zz',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] )



'''
Input: s = "abaccb", distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Output: true
Explanation:
- 'a' appears at indices 0 and 2 so it satisfies distance[0] = 1.
- 'b' appears at indices 1 and 5 so it satisfies distance[1] = 3.
- 'c' appears at indices 3 and 4 so it satisfies distance[2] = 0.
Note that distance[3] = 5, but since 'd' does not appear in s, it can be ignored.
Return true because s is a well-spaced string.
'''

'''
Input: s = "aa", distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Output: false
Explanation:
- 'a' appears at indices 0 and 1 so there are zero letters between them.
Because distance[0] = 1, s is not a well-spaced string.
'''



