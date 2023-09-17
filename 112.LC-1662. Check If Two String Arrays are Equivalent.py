# ()
'''
1662. Check If Two String Arrays are Equivalent

1.Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
2.Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false
3.Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true
'''
def check(word1,word2):
    new1 = new2 =''
    for i in word1:
        new1 = new1 + i
        
    for i in word2:
        new2 = new2 + i
    print(new1,new2)
    if (new1==new2):
        return True
    else:
        return False



check( ["ab", "c"], word2 = ["a", "bc"])
check( word1  = ["abc", "d", "defg"], word2 = ["abcddefg"] )
