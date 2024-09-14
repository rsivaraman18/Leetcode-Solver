


"""1648 Count the Number of Consistent Strings """


def countConsistentStrings(allowed,words):
    count = 0
    callowed = list(allowed)
    for word in words:
        flag = False
        for each in list(word):
            if each in allowed:
                flag = True
            else:
                flag = False
                break
        if flag == True:
            count += 1 
    print('Count:',count)



countConsistentStrings(allowed = "ab", words = ["ad","bd","aaab","baa","badab"])
countConsistentStrings(allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"])
countConsistentStrings(allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"])

"""

xample 1:

Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
Example 2:

Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7
Explanation: All strings are consistent.
Example 3:

Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4
Explanation: Strings "cc", "acd", "ac", and "d" are consistent.
"""