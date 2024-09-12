''' 917. Reverse Only Letters  '''

def revsolution1(s):
    l = 0
    s = list(s)
    r = len(s)-1
    while l<r:
        while not s[l].isalpha() and l<r:
            l = l+1
        while not s[r].isalpha() and l<r:
            r = r-1
            
        s[l],s[r] = s[r] ,s[l]
        l=l+1
        r=r-1
    res =  ''.join(s)
    print(res)       

revsolution1(s ="a-bC-dEf-ghIj")
revsolution1("Test1ng-Leet=code-Q!")

print('**************************')

def revsolution2(s):
    sent = list(s)
    i = 0
    j = len(sent)-1
    while i<j:
        if sent[i].isalpha() and sent[j].isalpha():
            sent[i],sent[j] = sent[j],sent[i]
            i= i+1
            j= j-1
            
        if not sent[i].isalpha():
            i = i+1
            
        if not sent[j].isalpha():
            j = j-1
            
    res = ''.join(sent)
    print(res)


revsolution2( "a-bC-dEf-ghIj")
revsolution2( "Test1ng-Leet=code-Q!")
