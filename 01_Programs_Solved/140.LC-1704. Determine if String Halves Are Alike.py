''' 1704. Determine if String Halves Are Alike '''

def vowels(s):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    slen = int(len(s))
    lword = s[0:int(slen/2)]
    rword = s[int(slen/2):slen]

    lcount = rcount = 0
    
    for i in lword:
        if i in vowels:
            lcount = lcount +1
            
    for i in rword:
        if i in vowels:
            rcount = rcount +1
    
    if lcount== rcount:
        print('True')
    else:
        print('False')

    
    

    
vowels(s = "book")
vowels("textbook")



    

'''
Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
'''

'''
Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.
'''
