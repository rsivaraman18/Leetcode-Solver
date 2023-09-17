#  ( )
''' 1876. Substrings of Size Three with Distinct Characters  '''

def dist(s ):
    d = { }
    count = 0
    for char in s:
        d[char] = d.get(char,0) + 1
    print(d )
        
            
    for key in d:
        if d[key] >1:
            count = count + 1
        
    print(count)



dist( s = "xyzzaz" )
dist(  s = "aababcabc" )
