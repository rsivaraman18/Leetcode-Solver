# ()
''' 2053	
Kth Distinct String in an Array  '''
def kdistinct(arr,k):
    d = { }
    for i in arr:
        d[i] = d.get(i,0) +1
    #print(d)
    out = [ ]
    for key,value in d.items():
        if value==1:
            out.append(key)
    print(out)
    

    try:
        dist = out[k-1]
        print(dist)
        return dist
    except:
        print('')
        return ''
    print('***********')       
   
kdistinct(["d","b","c","b","c","a"],2)    # a
kdistinct( ["aaa","aa","a"], k = 1)       #aaa
kdistinct( arr = ["a","b","a"],k = 3)   # ''
