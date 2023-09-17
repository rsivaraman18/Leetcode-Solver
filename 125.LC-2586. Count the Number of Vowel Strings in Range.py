''' 2586. Count the Number of Vowel Strings in Range    '''
# ()

def vowel(words,left,right):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    newlist = []
    words = words[left:right+1]
    for i in words:
        first = i[0]
        last  = i[-1]
        
        if (first in vowels) & (last in vowels):
            newlist.append(i)
    
            
    print(newlist)
    print(len(newlist))
        
    







vowel(["are","amy","u"] ,left = 0, right = 2)
vowel(["hey","aeo","mu","ooo","artro"],left = 1, right = 4)
vowel(["hey","aeo","mu","ooo","artro"],left=1,right=4)



'''
Input: words = ["are","amy","u"], left = 0, right = 2
Output: 2
Explanation: 
- "are" is a vowel string because it starts with 'a' and ends with 'e'.
- "amy" is not a vowel string because it does not end with a vowel.
- "u" is a vowel string because it starts with 'u' and ends with 'u'.
The number of vowel strings in the mentioned range is 2.
'''

'''
Input: words = ["hey","aeo","mu","ooo","artro"], left = 1, right = 4
Output: 3
Explanation: 
- "aeo" is a vowel string because it starts with 'a' and ends with 'o'.
- "mu" is not a vowel string because it does not start with a vowel.
- "ooo" is a vowel string because it starts with 'o' and ends with 'o'.
- "artro" is a vowel string because it starts with 'a' and ends with 'o'.
The number of vowel strings in the mentioned range is 3.
'''
