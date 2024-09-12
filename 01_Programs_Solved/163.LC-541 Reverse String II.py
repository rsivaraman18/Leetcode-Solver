''' 541. Reverse String II '''
''' Output: "bacdfeg" '''

def rev_word(s,k):
    out = []
    for i in range(0,len(s),k):
        new = s[i:i+k]
        out.append(new)
    print(out)
    res = ''
    for i in range(len(out)):
        if i%2!=0:
            res += out[i]
        else:
            reverse = out[i]
            res += reverse[::-1]
    return(res)
        
rev_word("abcdefg", 2)
rev_word("abcd", 2)


'''
if slen > k:
        new1 = s[0:k]
        rnew = new1[::-1]
        new2 = s[k:]
        print( rnew + new2 )
    else:
        print( s[::-1])'''
