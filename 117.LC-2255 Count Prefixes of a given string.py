'''
# 2255	
Count Prefixes of a Given String

Input: words = ["a","b","c","ab","bc","abc"], s = "abc"
Output: 3
Explanation:
The strings in words which are a prefix of s = "abc" are:
"a", "ab", and "abc".
Thus the number of strings in words which are a prefix of s is 3.
'''

'''
Input: words = ["a","a"], s = "aa"
Output: 2
Explanation:
Both of the strings are a prefix of s. 
Note that the same string can occur multiple times in words, and it should be counted each time.
'''


def CountPrefix(words,s):
    out = ''
    s1 = []
    count = 0
    for i in s:
        out = out + i
        s1.append(out)

    for i in words:
        if i in s1:
            count = count + 1
    print (count)
        
        
        
    

CountPrefix(["a","b","c","ab","bc","abc"] ,"abc" )
