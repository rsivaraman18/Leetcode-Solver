
'''
Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
'''

'''
Input: sentence = "leetcode"
Output: false
'''

def cword(s):
    s1 = set(sentence)
    s2 = len(s1)
    if (s2==26):
        return True
    else:
        return False
    



cword("thequickbrownfoxjumpsoverthelazydog")
cword("leetcode")
