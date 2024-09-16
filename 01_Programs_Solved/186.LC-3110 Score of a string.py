## 3110. Score of a string

def scoreOfString(s):
    max_length = len(s)
    total = 0
    for i in range(max_length):
        if (i<(max_length-1)): 
            a = ord(s[i])
            b = ord(s[i+1])
            val = abs(a-b)
            total += val
    print('total:',total)
    return total


scoreOfString(s = "hello")
scoreOfString("zaz")




# def scoreOfString(s):
#     mylist = []
#     for letter in s:
#         mylist.append(ord(letter))
#     print(mylist)
#     total = 0
    
#     for i in range(len(mylist)):
#         if (i<len(mylist)-1):           #0,1,2,3,4       #5
#             val = abs(mylist[i] - mylist[i+1])
#             total += val
#         else:pass
#     print('total:',total)



