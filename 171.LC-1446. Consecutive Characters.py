'''  1446. Consecutive Characters '''
def maxPower(s):
    box = '0'
    for letter in s:
        if letter == box[-1]:
            box +=letter
        else:
            box = box + ' ' + letter
    result = box.split()
    print(result)
 
    max_length_word = max(result, key=len) # Important step 
    max_length = len(max_length_word)
    print(max_length)

    

maxPower( s = "leetcode")
maxPower( s = "abbcccddddeeeeedcba")

'''
['0', 'l', 'ee', 't', 'c', 'o', 'd', 'e']
['0', 'a', 'bb', 'ccc', 'dddd', 'eeeee', 'd', 'c', 'b', 'a']
'''
