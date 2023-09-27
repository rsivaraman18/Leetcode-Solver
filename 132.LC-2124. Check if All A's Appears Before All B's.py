''' 2124. Check if All A's Appears Before All B's '''

''' 
Given a string s consisting of only the characters 'a' and 'b',
return true if every 'a' appears before every 'b' in the string.
Otherwise, return false.
'''

def check(s):
    slen = len(s)
    d = { }
    for i in s:
        if i=='a':
            d['a'] = d.get('a',0) + 1
        else:
            d['b'] = d.get('b',0) + 1
    print( d)
        
    # make string
    out = 'a'*d.get('a',0) + 'b'*d.get('b',0)
    print(out)

    # Compare strings
    if s==out:
        print('True')
    else:
        print('False')
check("aaabbb")
check("abab")
