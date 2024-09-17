### Both Method Solved the Answer
'''
Example 1:

Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.
Example 2:

Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".
Example 3:

Input: words = ["blue","green","bu"]
Output: []
Explanation: No string of words is substring of another string.
'''


def stringMatching(words):
    result = []
    for i,word in enumerate(words):
        sublist = words[:i] + words[i+1:]
        for each in sublist:
            if each in word and each not in result:
                result.append(each)
    print('Result',result)
    return result




def stringMatching(words):
    result = set()
    for i,word in enumerate(words):
        sublist = words[:i] + words[i+1:]
        for each in sublist:
            if each in word:
                result.add(each)
    print('Result',list(result))
    return list(result)


stringMatching(words = ["mass","as","hero","superhero"])
stringMatching(words = ["leetcode","et","code"])
stringMatching(["leetcoder","leetcode","od","hamlet","am"])

