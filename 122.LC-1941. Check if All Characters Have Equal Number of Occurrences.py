'''1941. Check if All Characters Have Equal Number of Occurrences'''


def instring1(s):
    li    = [ ]
    slen   = len(s)
    myset  = set(s)
    mysetlen = len(myset)

    for i in myset:
        new = s.count(i)
        li.append(new)
    print(li)
    
    for item in li:
        if li[0] != item:
            return False
            print("Not Equal")
            break
    else:
        #return True
        print("Equal")
            
      
    
    
    



instring1( "abacbc")
instring1( "aaabb")
