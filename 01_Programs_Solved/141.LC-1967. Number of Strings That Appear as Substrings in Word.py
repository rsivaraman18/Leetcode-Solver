''' 1967. Number of Strings That Appear as Substrings in Word

Given an array of strings patterns and a string word, return the number of strings in patterns that exist as a substring in word.

A substring is a contiguous sequence of characters within a string.
'''



def compare(patterns,word):
    count = 0
    for each in patterns:
        if each in word:
            count = count + 1
    print(count)
        


compare(["a","abc","bc","d"], word = "abc")
compare(["a","b","c"], word = "aaaaabbbbb")
compare(["a","a","a"], word = "ab")





'''
Input: patterns = ["a","abc","bc","d"], word = "abc"
Output: 3
Explanation:
- "a" appears as a substring in "abc".
- "abc" appears as a substring in "abc".
- "bc" appears as a substring in "abc".
- "d" does not appear as a substring in "abc".
3 of the strings in patterns appear as a substring in word.
'''
