
'''
Merging Of two strings alternatively
1. str1: abc   str2: pqr
2. str2: ab    str2: pqrs
''''

def merge2(word1,word2):
    print('Success on leet code')
    print('Given ','word1:',word1, '\tword2:',word2)
    new = ''
    s1 = str(word1)
    s2 = str(word2)
    list1 = [ ] 
    i=j=0
    while ( (i<len(s1)) or (j<len(s2))  ):
        output = ''
        
        if i<len(s1):
            output = output + s1[i]
            i = i +1
            
        if (j<len(s2)):
            output = output + s2[j]
            j = j +1

        list1.append(output)
        
    print('merged list is ',list1)
    merged = ''.join(list1)
    print('merged string is ',merged)
    print('*'*45 )
    



merge2("abc" ,"pqr")
merge2("ab" ,"pqrs")

#******************************************************

def mer():
    a = 'aaa'
    b = 'zzzz'
    la = len(a)
    lb = len(b)
    big = la if (la > lb) else lb
    res = ''
    for i in range(big):
        if i <la:
            res = res + a[i]
        if i<lb:
            res = res + b[i]
    print(res)
mer()
