"""
 2828.Check if a string is acronym of the word
Example 1:

Input: words = ["alice","bob","charlie"], s = "abc"
Output: true
Explanation: The first character in the words "alice", "bob", and "charlie" are 'a', 'b', and 'c', respectively. Hence, s = "abc" is the acronym. 
Example 2:

Input: words = ["an","apple"], s = "a"
Output: false
Explanation: The first character in the words "an" and "apple" are 'a' and 'a', respectively. 
The acronym formed by concatenating these characters is "aa". 
Hence, s = "a" is not the acronym.
Example 3:

Input: words = ["never","gonna","give","up","on","you"], s = "ngguoy"
Output: true
Explanation: By concatenating the first character of the words in the array, we get the string "ngguoy". 
Hence, s = "ngguoy" is the acronym.
"""

def isAcronym(words,s):
    result = ''
    for word in words:
        result += word[0]
    if result == s:
        print('True')
        return True
    else:
        print('false')
        return False







isAcronym(words = ["alice","bob","charlie"], s = "abc")
isAcronym(words = ["an","apple"], s = "a")
isAcronym(["never","gonna","give","up","on","you"], s = "ngguoy")
