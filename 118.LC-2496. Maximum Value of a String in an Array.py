'''2496. Maximum Value of a String in an Array'''

'''
Input: strs = ["alic3","bob","3","4","00000"]
Output: 5
'''

'''
Input: strs = ["1","01","001","0001"]
Output: 1
'''


# ()

def Maxstring(strs):
    li = []
    for i in strs:
        if i.isnumeric() == True:
            new = int(i)
            li.append(new)
            
        else:
            new = len(i)
            li.append(new)
    print(li)
    print(max(li))
    




Maxstring(["alic3","bob","3","4","00000"])
Maxstring( ["1","01","001","0001"])



