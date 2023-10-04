''' 1160. Find Words That Can Be Formed by Characters '''

def characters(words,chars):
    finList = []
    for word in words:
        count = 0
        for each in word:
            if each in chars:
                count = count +1
        if len(word) == count:
            finList.append(word)
    print(finList)

    result = 0
    for each in finList:
        result = result + len(each)
    print(result)
        

characters(words = ["cat","bt","hat","tree"], chars = "atach")
characters( ["hello","world","leetcode"], chars = "welldonehoneyr" )


'''
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
'''
