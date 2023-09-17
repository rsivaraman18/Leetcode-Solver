''' 2138. Divide a String Into Groups of Size k '''

def splitword(s,k,fill):
    result = []
    for i in range (0,len(s),k):
        if i+k <=len(s):
            new = s[i:i+k]
            result.append(new)
            
        else:
            diff = len(s) - i
            new = s[i:i+diff]
            lnew = len(new)
            new = new + fill*(k-lnew)
            result.append(new)
            
    print(result)
    

#splitword( s = "abcdefghi", k = 3, fill = "x" )
#splitword( s = "abcdefghij", k = 3, fill = "x" )
splitword("ctoyjrwtngqwt",8,'n')


def split():
    s= 'abcdefghij'
    k = 3
    fill = 'x'
    
    rem  = len(s)%k
    new = s + fill*(k-rem)
    print(new)

    while len(new)>0:
        res = new[:3]
        print(res)
        new = new[3:]
        

split()

