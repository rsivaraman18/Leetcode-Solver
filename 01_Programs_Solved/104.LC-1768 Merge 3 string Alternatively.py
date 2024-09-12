
'''
Merging Of THREE strings alternatively
1. str1: abcDEFG   str2: XYZ  STR3 :12345
2. 
''''

def merge3(s1,s2,s3):
    print('Given String1:',s1 ,'\tString2: ',s2,'\tString3: ',s3 )
    s1 = str(s1)
    s2 = str(s2)
    s3 = str(s3)
    list1 = [ ] 
    i=j=k=0
    while ( (i<len(s1)) or (i<len(s2)) or (i<len(s3)) ):
        output = ''
        
        if i<len(s1): 
            output = output + s1[i]
            i = i +1
            
        if (j<len(s2)): 
            output = output + s2[j]
            j = j +1
            
        if (k<len(s3)):
            output = output + s3[k]
            k = k +1
        list1.append(output)
        
    
    print('merged string',list1)
    merged = ''.join(list1 )
    print('merged string',merged)
    print('*'*45 )
            

def merge():
    a = 'aaa'
    b = 'zzzz'
    c = 'sssss'
    
    la ,lb,lc = len(a) ,len(b),len(c)
    
    big = la if  ((la > lb)& (la > lc))  else lb if (lb> lc) else lc
    res = ''
    for i in range(big):
        if i <la:
            res = res + a[i]
        if i<lb:
            res = res + b[i]
        if i<lc:
            res = res + c[i]
    print('3 merged word',res)
        
        


merge()


#merge3('abcdefg','xyz',12345)
