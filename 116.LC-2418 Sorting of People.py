def height(names,heights):   
    d  = { }
    li = []
    for i in range(len(names)):
        d[heights[i]] = names[i]
    d1 = sorted(d,reverse=True)
    
    for i in d1:
        li.append(d[i])
    
    print(li)



height(["Mary","John","Emma"],[180,165,170] )
height(["Alice","Bob","Bob"] , [155,185,150] )












'''
2418. Sort the People

Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]
Explanation: Mary is the tallest, followed by Emma and John.


Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
Output: ["Bob","Alice","Bob"]
Explanation: The first Bob is the tallest, followed by Alice and the second Bob.

'''
